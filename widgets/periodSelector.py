
from PySide6.QtGui import QPainter, QColor, QPen,QBrush
from PySide6.QtCore import Qt, QPointF, QPoint, QRect,QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QCheckBox,QPushButton
import math
from PySide6.QtCore import Signal

# class SettingsWindow(QWidget):
#     def __init__(self, period_selector_widget, parent=None):
#         super().__init__(parent)
#         self.period_selector_widget = period_selector_widget
#         self.setWindowFlag(Qt.WindowStaysOnTopHint)

#         layout = QVBoxLayout()

#         self.radius_slider = QSlider(Qt.Horizontal)
#         self.radius_slider.setMinimum(0)
#         self.radius_slider.setMaximum(200)
#         self.radius_slider.setValue(self.period_selector_widget.radius)
#         self.radius_slider.valueChanged.connect(self.update_radius)
#         layout.addWidget(QLabel("Radius:"))
#         layout.addWidget(self.radius_slider)

#         self.second_radius_slider = QSlider(Qt.Horizontal)
#         self.second_radius_slider.setMinimum(0)
#         self.second_radius_slider.setMaximum(200)
#         self.second_radius_slider.setValue(self.period_selector_widget.second_radius)
#         self.second_radius_slider.valueChanged.connect(self.second_update_radius)
#         layout.addWidget(QLabel("Second Radius:"))
#         layout.addWidget(self.second_radius_slider)

#         self.speed_slider = QSlider(Qt.Horizontal)
#         self.speed_slider.setMinimum(0)  # Минимальная скорость
#         self.speed_slider.setMaximum(200)  # Максимальная скорость
#         self.speed_slider.setValue(0)  # Начальное значение скорости
#         self.speed_slider.valueChanged.connect(self.update_speed)
#         layout.addWidget(QLabel("Speed:"))
#         layout.addWidget(self.speed_slider)

#         self.close_button = QPushButton("Close")
#         self.close_button.clicked.connect(lambda: QApplication.quit())
#         layout.addWidget(self.close_button)

#         self.setLayout(layout)
#         self.setWindowTitle("Settings")

#         # Создаем таймер для кручения
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.rotate_period)
#         self.update_speed(self.speed_slider.value())  # Установка начальной скорости
#         self.timer.start(1000000)  # Интервал в миллисекундах

#     def update_radius(self, value):
#         self.period_selector_widget.radius = value
#         self.period_selector_widget.update()

#     def second_update_radius(self, value):
#         self.period_selector_widget.second_radius = value
#         self.period_selector_widget.update()

#     def update_speed(self, value):
#         # Обновление интервала таймера в зависимости от значения слайдера скорости
#         if value != 0:
#             self.timer.setInterval(2000 / value)
#         else:
#             self.timer.setInterval(100000000)

#     def rotate_period(self):
#         start, end = self.period_selector_widget.selected_period
#         start = (start + 1) % 24  # Увеличиваем начало периода на 1, зацикливая его от 0 до 23
#         end = (end + 1) % 24      # То же самое для конца периода
#         #print(start,end)
#         self.period_selector_widget.selected_period = (start, end)
#         self.period_selector_widget.update()

#--------------------------------

class PeriodSelector(QWidget):
    periodChanged = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setMinimumSize(200, 200)
        self.selected_period = (9, 22)
        self.is_dragging = False
        self.ellips_dragging = None

        self.center = QPoint(100, 100)
        self.radius = 55
        self.second_radius = 15
        self.pb_color = QColor(0, 0, 255)
        self.bg_color = QColor(0, 0, 0, 51)

        self.border_color = QColor(255, 255, 255)
        self.border_width = 2        

        self.text_color = QColor(200, 200, 200)
        self.text_size = 8
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(self.border_color, self.border_width, Qt.SolidLine))
        painter.drawEllipse(self.center,self.radius,self.radius)
        painter.drawEllipse(self.center,self.radius+self.second_radius,self.radius+self.second_radius)

        start_angle, span_angle = self.getDegreesFromPeriod(self.selected_period)

        rect = QRect(self.center.x() - self.radius - self.second_radius/2 ,
                     self.center.y() - self.radius - self.second_radius/2 ,
                     self.radius *2 + self.second_radius ,
                     self.radius *2 + self.second_radius )
        
        painter.setPen(QPen(self.bg_color, self.second_radius, Qt.SolidLine))
        painter.drawArc(rect, 0 * 16, 360 * 16)

        painter.setPen(QPen(self.pb_color, self.second_radius-self.border_width, Qt.SolidLine))
        painter.drawArc(rect, start_angle*16, -span_angle*16)

        EllipseSize = ((self.second_radius + self.border_width)*1.1)
        start_x = self.center.x() - EllipseSize/2 + (self.radius+self.second_radius/2) * math.cos(math.radians(start_angle))
        start_y = self.center.y() - EllipseSize/2 + (self.radius+self.second_radius/2) * math.sin(math.radians(-start_angle))
        end_x = self.center.x() - EllipseSize/2 + (self.radius+self.second_radius/2) * math.cos(math.radians(-(self.makePositivePi(start_angle - span_angle))))
        end_y = self.center.y() - EllipseSize/2 + (self.radius+self.second_radius/2) * math.sin(math.radians(-(self.makePositivePi(start_angle - span_angle))))

        # Нарисовать эллипс вокруг начала и конца выбранного периода
        painter.setPen(QPen(self.bg_color, self.border_width, Qt.SolidLine))
        painter.setBrush(self.pb_color) 
        painter.drawEllipse(start_x, start_y, EllipseSize, EllipseSize)
        painter.drawEllipse(end_x, end_y, EllipseSize, EllipseSize)

        marker_color = QColor(self.border_color.red(), self.border_color.green(), self.border_color.blue(), 51)
        painter.setPen(QPen(marker_color, 2, Qt.SolidLine))
        for i in range(24):
            angle = i * 15 - 90  # Вычисляем угол для текущего деления
            x1 = self.center.x() + (self.radius+self.second_radius) * math.cos(math.radians(angle))
            y1 = self.center.y() + (self.radius+self.second_radius) * math.sin(math.radians(angle))
            x2 = self.center.x() + self.radius * math.cos(math.radians(angle))  # Увеличиваем радиус для линии деления
            y2 = self.center.y() + self.radius * math.sin(math.radians(angle))  # Увеличиваем радиус для линии деления
            painter.drawLine(x1, y1, x2, y2)

        painter.setPen(QPen(self.text_color, 0, Qt.SolidLine))
        font = painter.font()
        font.setPointSize(self.text_size)
        painter.setFont(font)
        for i in range(24, 0, -1):  # Изменен порядок итерации
            angle = (24-i) * 15 - 90
            x = self.center.x() + (self.radius+self.second_radius+10) * math.cos(math.radians(angle))
            y = self.center.y() + (self.radius+self.second_radius+10) * math.sin(math.radians(-angle))
            
            # Получаем ширину и высоту текста
            font_metrics = painter.fontMetrics()
            text_width = font_metrics.horizontalAdvance(str(i))
            text_height = font_metrics.ascent() + font_metrics.descent()
            
            # Корректируем координаты для выравнивания по центру
            x -= text_width / 2
            y += text_height / 4
            
            painter.drawText(x, y, str(i))
                
    def getDegreesFromPeriod(self,period):
        start_angle = -90 + -15 * period[0]
        if period[1] >= period[0]:
            span_angle = (period[1] - period[0]) * 15
        else:
            span_angle = (24 + period[1] - period[0]) * 15
        start_angle = self.makePositivePi(start_angle)
        span_angle = self.makePositivePi(span_angle)
        return (start_angle,span_angle)
    
    def get_side_period(self, pos):
        period_start, period_end = self.selected_period
        angle_degrees = self.getDegree(pos)
        if  self.ellips_dragging == 'e1':
            period_start = round(self.makePositivePi(360-angle_degrees-90)/15)
        elif  self.ellips_dragging == 'e2':
            period_end = round(self.makePositivePi(360-angle_degrees-90)/15)
        return period_start, period_end

    def get_period(self, pos,offset):
        angle_degrees = self.getDegree(pos)
        period_start, period_end = self.selected_period
        diff = (period_end - period_start) if period_end > period_start else (24 + period_end - period_start)
        period_start = round((360-angle_degrees+offset-90) / 15) % 24
        period_end = (period_start + diff) % 24
        return period_start, period_end
    
    def getDegree(self, pos, calculate_distance=False):
        center = self.center
        centered = QPointF(pos.x() - center.x(), center.y() - pos.y())
        angle = math.atan2(centered.y(), centered.x())
        angle_degrees = self.makePositivePi(math.degrees(angle))
        if calculate_distance:
            distance = math.sqrt(centered.x() * centered.x() + centered.y() * centered.y())
            return angle_degrees, distance
        return angle_degrees

    def makePositivePi(self,degrees):
        return (degrees % 360 + 360) % 360
    
    def resizeEvent(self, event):
        self.center = QPoint(self.width() / 2, self.height() / 2)
        self.update()

    #----------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            click_pos = event.pos()            
            angle_degrees, distance = self.getDegree(click_pos,True)

            start_angle, span_angle = self.getDegreesFromPeriod(self.selected_period)
            self.offset = angle_degrees-start_angle
            end_angle = self.makePositivePi(start_angle-span_angle)
            
            if self.radius <= distance <= self.radius+self.second_radius:
                if start_angle - 10 <= angle_degrees <= start_angle + 10:
                    self.ellips_dragging = "e1"
                    # print("e1")
                elif end_angle - 10 <= angle_degrees <= end_angle + 10:
                    self.ellips_dragging = "e2"
                    # print("e2")
                else:
                    if start_angle > end_angle:  # Если start_angle меньше end_angle
                        if start_angle >= angle_degrees >= end_angle:
                            self.is_dragging = True
                            # print("drag")
                    else:  # Если end_angle меньше start_angle
                        if angle_degrees <= start_angle or angle_degrees >= end_angle:
                            self.is_dragging = True
                            # print("drag")

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            move_pos = event.pos()
            self.selected_period = self.get_period(move_pos,self.offset)
            self.update()
            
        elif self.ellips_dragging != None:
            move_pos = event.pos()
            self.selected_period = self.get_side_period(move_pos)
            self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            self.ellips_dragging = None
            self.periodChanged.emit()

# app = QApplication([])

# widget = PeriodSelector()
# widget.setGeometry(400, 400, 400, 400)
# widget.show()

# settings_window = SettingsWindow(widget)
# settings_window.setGeometry(400, 200, 200, 200)
# settings_window.show()

# app.exec_()