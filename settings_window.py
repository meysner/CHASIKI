from PySide6.QtWidgets import QDialog, QLabel, QSpinBox, QSlider, QPushButton, QVBoxLayout, QColorDialog, QFrame, QHBoxLayout
from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import *

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 300, 150)
        self.setMaximumSize(300, 300)

        self.start_hour_spinbox = QSpinBox(minimum=0, maximum=24)

        self.end_hour_spinbox = QSpinBox(minimum=0, maximum=24)

        self.pg_color_label = QLabel("Pick a color of progress bar:")
        self.pg_color_button = QPushButton("Choose a color")
        self.pg_color = self.parent().progress_bar_color
        self.pg_color_button.clicked.connect(lambda: self.showColorDialog(self.pg_color, self.pg_color_label))

        self.outline_pg_color_label = QLabel("Pick a color of outline")
        self.outline_pg_color_button = QPushButton("Choose a color")
        self.outline_pg_color = self.parent().outline_color
        self.outline_pg_color_button.clicked.connect(lambda: self.showColorDialog(self.outline_pg_color, self.outline_pg_color_label))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)

        self.save_button = QPushButton("Apply")
        self.save_button.clicked.connect(self.saveSettings)

        self.color = QColor(0, 128, 255)

        startHour_layout = QHBoxLayout()
        startHour_layout.addWidget(QLabel("Start Hour:"))
        startHour_layout.addWidget(self.start_hour_spinbox)

        endHour_layout = QHBoxLayout()
        endHour_layout.addWidget(QLabel("End Hour:"))
        endHour_layout.addWidget(self.end_hour_spinbox)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)

        layout = QVBoxLayout(self)
        layout.addLayout(startHour_layout)
        layout.addLayout(endHour_layout)
        layout.addWidget(separator)
        layout.addWidget(self.pg_color_label)
        layout.addWidget(self.pg_color_button)
        layout.addWidget(self.outline_pg_color_label)
        layout.addWidget(self.outline_pg_color_button)
        layout.addWidget(QLabel("Corner radius:"))
        layout.addWidget(self.slider)
        layout.addWidget(self.save_button)

    def showColorDialog(self, color_var, label):
        color_dialog = QColorDialog(self)
        if color_dialog.exec_():
            color = color_dialog.currentColor()
            self.updateColorLabel(color, label)
            color_var.setRgb(color.red(), color.green(), color.blue())

    def updateColorLabel(self, color, label):
        color_name = color.name()
        style_sheet = f"background-color: {color_name};"
        label.setStyleSheet(style_sheet)

    def saveSettings(self):
        start_hour = self.start_hour_spinbox.value()
        end_hour = self.end_hour_spinbox.value()
        window_corner_radius = self.slider.value()
        progress_bar_color = self.pg_color
        outline_progress_bar_color = self.outline_pg_color

        self.parent().updateSettings(start_hour, end_hour, window_corner_radius, progress_bar_color,outline_progress_bar_color)
        self.accept()
