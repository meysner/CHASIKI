from PySide6.QtWidgets import QDialog, QLabel, QSpinBox, QSlider, QPushButton, QVBoxLayout, QColorDialog
from PySide6.QtGui import QColor,Qt

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 300, 150)

        self.color_label = QLabel("Pick a color of progress bar:")
        self.color_button = QPushButton("Choose a color")
        self.color_button.clicked.connect(self.showColorDialog)

        self.start_hour_label = QLabel("Start Hour:")
        self.start_hour_spinbox = QSpinBox()
        self.start_hour_spinbox.setMinimum(0)
        self.start_hour_spinbox.setMaximum(24)

        self.end_hour_label = QLabel("End Hour:")
        self.end_hour_spinbox = QSpinBox()
        self.end_hour_spinbox.setMinimum(0)
        self.end_hour_spinbox.setMaximum(24)

        self.slider_label = QLabel("Corner radius:")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)

        self.save_button = QPushButton("Apply")
        self.save_button.clicked.connect(self.saveSettings)

        self.color = QColor(0, 128, 255)  

        layout = QVBoxLayout(self)
        layout.addWidget(self.color_label)
        layout.addWidget(self.color_button)
        layout.addWidget(self.start_hour_label)
        layout.addWidget(self.start_hour_spinbox)
        layout.addWidget(self.end_hour_label)
        layout.addWidget(self.end_hour_spinbox)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.save_button)

    def showColorDialog(self):
        color_dialog = QColorDialog(self)
        if color_dialog.exec_():  
            self.color = color_dialog.currentColor()
            self.updateColorLabel()

    def updateColorLabel(self):
        color_name = self.color.name()
        style_sheet = f"background-color: {color_name};"
        self.color_label.setStyleSheet(style_sheet)

    def saveSettings(self):
        start_hour = self.start_hour_spinbox.value()
        end_hour = self.end_hour_spinbox.value()
        window_corner_radius = self.slider.value()
        progress_bar_color = self.color

        self.parent().updateSettings(start_hour, end_hour, window_corner_radius, progress_bar_color)
        self.accept()
