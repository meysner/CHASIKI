from PySide6.QtCore import Qt, QTimer, QTime, QPoint
from PySide6.QtWidgets import QMainWindow, QMenu, QApplication, QWidget, QSizeGrip
from PySide6.QtGui import QColor, QAction
from settings_window import SettingsWindow
from widgets.progress_widget import ProgressWidget
import utils

class ProgressBarWindow(QMainWindow):
    def __init__(self, config):
        super(ProgressBarWindow, self).__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.config = config
        self.readConfigProperties()
        self.current_time = QTime.currentTime()

        self.progress_widget = ProgressWidget(self)
        self.setCentralWidget(self.progress_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(60000)

        self.dragging = False
        self.offset = None

        self.context_menu = QMenu(self)
        
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.showSettings)
        self.context_menu.addAction(settings_action)

        close_action = QAction("Exit", self)
        close_action.triggered.connect(self.close)
        self.context_menu.addAction(close_action)

        self.settings_window = SettingsWindow(self)

        # QSizeGrip for resizing
        self.gripSize = 5
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.setStyleSheet("background-color: transparent;")
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)
        

    def resizeEvent(self, event):
        super().resizeEvent(event)
        rect = self.rect()

        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.position()

    def mouseMoveEvent(self, event):
        if self.dragging:
            offset = event.position() - self.offset
            new_pos = self.pos() + QPoint(offset.x(), offset.y())
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.offset = None

    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())

    def showSettings(self):
        self.settings_window.period.selected_period = ((self.start_hour,self.end_hour))
        self.settings_window.show()

    def updateSettings(self, start_hour, end_hour, window_corner_radius, progress_bar_color, outline_color,outline,bg_color):
        self.config.Config['start_hour'] = start_hour
        self.config.Config['end_hour'] = end_hour
        
        self.config.Config['progress_bar_color'] = utils.QColor2Array(progress_bar_color)
        self.config.Config['window_corner_radius'] = window_corner_radius
        self.config.Config['outline_width'] = outline
        self.config.Config['outline_color'] = utils.QColor2Array(outline_color)
        self.config.Config["bg_color"] = utils.QColor2Array(bg_color)
        self.readConfigProperties()
        self.progress_widget.update()
        self.settings_window.update()
        

    def readConfigProperties(self):
        config = self.config
        self.start_hour = config.Config.get('start_hour')
        self.end_hour = config.Config.get('end_hour')
        
        self.progress_bar_color = utils.Array2QColor(config.Config.get('progress_bar_color'))
        self.window_corner_radius = config.Config.get('window_corner_radius')
        self.outline_width = config.Config.get('outline_width')
        self.outline_color = utils.Array2QColor(config.Config.get('outline_color'))
        self.bg_color = utils.Array2QColor(config.Config.get('bg_color'))
        self.update()

    def updateTime(self):
        self.current_time = QTime.currentTime()
        self.progress_widget.update()