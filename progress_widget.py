from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, QTimer

class ProgressWidget(QWidget):
    def __init__(self, parent):
        super(ProgressWidget, self).__init__(parent)

    def updateProgress(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        progress_rect = QRect(0, 0, self.width(), self.height())

        start_hour = self.parent().start_hour
        end_hour = self.parent().end_hour
        current_time = self.parent().current_time

        progress_bar_color = self.parent().progress_bar_color
        window_corner_radius = self.parent().window_corner_radius

        total_minutes = (end_hour - start_hour) * 60
        current_minutes = (current_time.hour() - start_hour) * 60 + current_time.minute()

        progress_percentage = current_minutes / total_minutes * 100
        progress_percentage = max(0, min(100, progress_percentage))

        outline_color = QColor(255, 255, 255)
        outline_pen = QPen(outline_color, 2)  
        painter.setPen(outline_pen)
        painter.setBrush(QColor(0, 0, 0, 51))
        painter.drawRoundedRect(progress_rect, window_corner_radius, window_corner_radius) 

        painter.setPen(outline_pen)
        painter.setBrush(progress_bar_color)
        progress_width = progress_rect.width() * (progress_percentage / 100)
        progress_rect.setWidth(progress_width)
        painter.drawRoundedRect(progress_rect, window_corner_radius, window_corner_radius)  

        for minute in range(0, total_minutes + 1, 60): 
            self.drawMinuteMarker(painter, minute, total_minutes, progress_rect)

    def drawMinuteMarker(self, painter, minute, total_minutes, progress_rect):
        marker_width = 2
        marker_rect = QRect(0, 0, marker_width, progress_rect.height())
        
        marker_left = (minute / total_minutes) * (self.width() - marker_width) + progress_rect.left()

        marker_rect.moveLeft(marker_left)

        painter.setPen(QPen(QColor(255, 255, 255, 51)))  
        painter.setBrush(QColor(255, 255, 255, 51)) 
        painter.drawRect(marker_rect)
