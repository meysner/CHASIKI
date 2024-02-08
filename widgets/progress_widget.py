from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect

class ProgressWidget(QWidget):
    def __init__(self, parent):
        super(ProgressWidget, self).__init__(parent)

    def updateProgress(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        start_hour = self.parent().start_hour
        end_hour = self.parent().end_hour
        current_time = self.parent().current_time

        if end_hour < start_hour: end_hour+=24

        progress_bar_color = self.parent().progress_bar_color
        window_corner_radius = self.parent().window_corner_radius
        outline = self.parent().outline_width
        outline_color = self.parent().outline_color
        bg_color = self.parent().bg_color

        total_minutes = abs((end_hour - start_hour) * 60)
        if current_time.hour() > start_hour:
            current_minutes = (current_time.hour() - start_hour) * 60 + current_time.minute()
        else:
            current_minutes = (current_time.hour()+24 - start_hour) * 60 + current_time.minute()
        progress_percentage = current_minutes / total_minutes * 100
        progress_percentage = max(0, min(100, progress_percentage))

        progress_rect = QRect(outline, outline, self.width() - outline*2, self.height() - outline*2)

        outline_pen = QPen(outline_color, outline)
        painter.setPen(outline_pen)
        painter.setBrush(bg_color)
        painter.drawRoundedRect(progress_rect, window_corner_radius, window_corner_radius) 

        painter.setPen(outline_pen)
        painter.setBrush(progress_bar_color)
        progress_width = progress_rect.width() * (progress_percentage / 100)
        progress_rect.setWidth(progress_width)
        painter.drawRoundedRect(progress_rect, window_corner_radius, window_corner_radius)  

        for minute in range(0, total_minutes, 60): 
            if minute == 0: continue
            self.drawMinuteMarker(painter, minute, total_minutes, progress_rect,outline,outline_color)

    def drawMinuteMarker(self, painter, minute, total_minutes, progress_rect, outline,outline_color):
        marker_width = 2
        marker_rect = QRect(outline, outline, marker_width, progress_rect.height())
        marker_left = (minute / total_minutes) * (self.width() - marker_width) + outline
        marker_rect.moveLeft(marker_left)

        marker_color = QColor(outline_color.red(), outline_color.green(), outline_color.blue(), 51)

        painter.setPen(QPen(marker_color))
        painter.setBrush(marker_color)
        painter.drawRect(marker_rect)