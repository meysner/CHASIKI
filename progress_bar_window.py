from PySide6.QtCore import Qt, QTimer, QTime, QPoint
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from settings_window import SettingsWindow
from progress_widget import ProgressWidget
from PySide6.QtGui import QColor

class ProgressBarWindow(QMainWindow):
    def __init__(self, start_hour, end_hour):
        super(ProgressBarWindow, self).__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.start_hour = start_hour
        self.end_hour = end_hour
        self.current_time = QTime.currentTime()

        self.progress_bar_color = QColor(0, 128, 255)
        self.window_corner_radius = 0

        self.progress_widget = ProgressWidget(self)
        self.setCentralWidget(self.progress_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

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

    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())

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

    def showSettings(self):
        self.settings_window.start_hour_spinbox.setValue(self.start_hour)
        self.settings_window.end_hour_spinbox.setValue(self.end_hour)
        self.settings_window.show()

    def updateSettings(self, start_hour, end_hour, window_corner_radius,progress_bar_color):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.progress_bar_color = progress_bar_color
        self.window_corner_radius = window_corner_radius
        self.progress_widget.update()

    def updateTime(self):
        self.current_time = QTime.currentTime()
        self.progress_widget.update()