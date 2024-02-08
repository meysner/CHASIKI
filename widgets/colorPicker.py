from PySide6.QtWidgets import QDialog,QSpacerItem , QLineEdit, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QStackedLayout, QSlider,QSizePolicy
from PySide6.QtGui import Qt, QColor, QPainter, QBrush, QPalette,QPixmap
from PySide6.QtGui import QPainter, QColor, QPen,QBrush
from PySide6.QtCore import Qt, QPointF, QPoint, QRect,QTimer,QSize
from PySide6.QtWidgets import QApplication, QWidget,QFrame , QVBoxLayout, QSlider, QLabel, QCheckBox,QPushButton
import math
import colorsys
from typing import Union
from PySide6.QtCore import Signal

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledaXnIfp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class ColorPicker(QDialog):
    def __init__(self, parent=None,hue=0,saturation=100,lightness=100,alpha=255):
        super().__init__(parent)
        self.setWindowTitle('Name')
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.dragging = False
        self.alpha = alpha
        self.hue = hue
        self.saturation = saturation
        self.lightness = lightness
        self.updateRGBA()
        self.setupUi(self)
        self.setColorSelector(self.saturation,self.lightness)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(220, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(220, 310))
        Dialog.setMaximumSize(QSize(220, 310))
        Dialog.setLayoutDirection(Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: #232323;\n"
"}")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 200, 300))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hue_slider = QSlider(self.layoutWidget)
        self.hue_slider.setObjectName(u"hue_slider")
        self.hue_slider.setAutoFillBackground(False)
        self.hue_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"    height: 10px;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"    border: 1px solid #777;\n"
"    width: 20px;\n"
"    margin-top: -5px;\n"
"    margin-bottom: -5px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #ccc;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background-color: #bbb;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background-color: #888;\n"
"}")
        self.hue_slider.setOrientation(Qt.Horizontal)
        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(359)
        self.hue_slider.setSingleStep(1)
        self.hue_slider.setValue(self.hue)
        self.hue_slider.valueChanged.connect(self.hue_changed)
        self.verticalLayout.addWidget(self.hue_slider)

        self.transparent_slider = QSlider(self.layoutWidget)
        self.transparent_slider.setObjectName(u"transparent_slider")
        self.transparent_slider.setAutoFillBackground(False)
        self.transparent_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255,255, 255, 0), stop:1 rgba(255, 255, 255, 255));\n"
"    height: 10px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"    border: 1px solid #777;\n"
"    width: 20px;\n"
"    margin-top: -5px;\n"
"    margin-bottom: -5px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #ccc;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background-color: #bbb;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background-color: #888;\n"
"}")
        self.transparent_slider.setOrientation(Qt.Horizontal)
        self.transparent_slider.setMinimum(0)
        self.transparent_slider.setMaximum(255)
        self.transparent_slider.setSingleStep(1)
        self.transparent_slider.setValue(self.alpha)
        self.transparent_slider.valueChanged.connect(self.transparent_changed)

        self.verticalLayout.addWidget(self.transparent_slider)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.color_indicator = QLabel(self.layoutWidget)
        self.color_indicator.setObjectName(u"label")
        self.color_indicator.setMinimumSize(QSize(50, 50))
        self.color_indicator.setMaximumSize(QSize(50, 50))
        self.color_indicator.setStyleSheet(u"QLabel{\n"
f"	background-color: rgba({self.rgba[0]},{self.rgba[1]},{self.rgba[2]},{self.rgba[3]});\n"
"	border-radius: 20px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.color_indicator)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.color_view = QFrame(self.layoutWidget)
        self.color_view.setObjectName(u"color_view")
        self.color_view.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.color_view.sizePolicy().hasHeightForWidth())
        self.color_view.setSizePolicy(sizePolicy1)
        self.color_view.setMinimumSize(QSize(200, 200))
        self.color_view.setMaximumSize(QSize(200, 200))
        self.color_view.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 hsv({self.hue},255,255));\n"
"margin: 0;\n"
"")
        self.color_view.setFrameShape(QFrame.StyledPanel)
        self.color_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.color_view)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.black_overlay = QFrame(self.color_view)
        self.black_overlay.setObjectName(u"black_overlay")
        sizePolicy1.setHeightForWidth(self.black_overlay.sizePolicy().hasHeightForWidth())
        self.black_overlay.setSizePolicy(sizePolicy1)
        self.black_overlay.setMinimumSize(QSize(200, 200))
        self.black_overlay.setMaximumSize(QSize(200, 200))
        self.black_overlay.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 4px;\n"
"margin: 0;\n"
"")
        self.black_overlay.setFrameShape(QFrame.StyledPanel)
        self.black_overlay.setFrameShadow(QFrame.Raised)
        self.selector = QFrame(self.black_overlay)
        self.selector.setObjectName(u"selector")
        self.selector.setGeometry(QRect(194, 20, 12, 12))
        self.selector.setMinimumSize(QSize(12, 12))
        self.selector.setMaximumSize(QSize(12, 12))
        self.selector.setStyleSheet(u"background-color:none;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.selector.setFrameShape(QFrame.StyledPanel)
        self.selector.setFrameShadow(QFrame.Raised)
        self.black_ring = QLabel(self.selector)
        self.black_ring.setObjectName(u"black_ring")
        self.black_ring.setGeometry(QRect(1, 1, 10, 10))
        self.black_ring.setMinimumSize(QSize(10, 10))
        self.black_ring.setMaximumSize(QSize(10, 10))
        self.black_ring.setBaseSize(QSize(10, 10))
        self.black_ring.setStyleSheet(u"background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.black_overlay)


        self.verticalLayout_3.addWidget(self.color_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        confirm_button = QPushButton('Confirm', self)
        confirm_button.clicked.connect(self.accept)

        cancel_button = QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.reject)

        self.horizontalLayout.addWidget(cancel_button)
        self.horizontalLayout.addWidget(confirm_button)

        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
        
    def mousePressEvent(self, event):
        click_pos = event.pos() 
        if self.color_view.geometry().contains(click_pos):
            self.dragging = True
            self.color_view_interact(click_pos)
    def mouseMoveEvent(self, event):
        if self.dragging:
            click_pos = event.pos() 
            self.color_view_interact(click_pos)
    def mouseReleaseEvent(self, event):
        self.dragging = False

    def color_view_interact(self,click_pos):
        self.saturation,self.lightness = self.getArgumentsByColorView(click_pos)
        self.indicator_update()
        self.selector.setGeometry(
    max(0, min(click_pos.x() - self.color_view.x() - 18, self.color_view.width() - 12)),
    max(0, min(click_pos.y() - self.color_view.y() - 18, self.color_view.height() - 12)),
    12,
    12
)

    def getArgumentsByColorView(self, click_pos):
        centred_pos = (click_pos.x() - self.color_view.x() - 10, click_pos.y() - self.color_view.y() - 10)
        shape = self.color_view.frameGeometry()
        shape = (shape.width(), shape.height())
        relative_value = (centred_pos[0] / shape[0], centred_pos[1] / shape[1])
        
        # Ограничение значений в диапазоне от 0 до 255
        x_value = max(0, min(relative_value[0] * 100, 100))
        y_value = max(0, min(100 - relative_value[1] * 100, 100))
        
        return (x_value, y_value)

    def indicator_update(self):
        self.updateRGBA()
        self.color_indicator.setStyleSheet(u"QLabel{\n"
f"	background-color: rgba({self.rgba[0]},{self.rgba[1]},{self.rgba[2]},{self.rgba[3]});\n"
"	border-radius: 20px;\n"
"}")

    def hue_changed(self, value):
        self.hue = value
        self.color_view.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 hsv({self.hue}, 255, 255));\n"
"margin: 0;\n"
"")
        self.indicator_update()

    def transparent_changed(self, value):
        self.alpha = value
        self.indicator_update()

    def setColorSelector(self,saturation,lithness):
        geometry = self.color_view.frameGeometry()
        print(geometry)

        x = max(self.color_view.x(), min(self.color_view.x()+self.saturation/100*geometry.width()-18, self.color_view.x()+geometry.width()))
        y = max(self.color_view.y(), min(self.color_view.y()+geometry.height() - self.lightness/100*geometry.height()-18, self.color_view.y()+geometry.height()))
        print(self.color_view.y(),geometry.height(),self.lightness/100*geometry.height())
        self.selector.setGeometry(
    x,
    y,
    12,
    12
)


    def selector_convert(self,x,y):
        x = x + self.color_view.x()
        y = y + self.color_view.x()
        return (x,y)

    def updateRGBA(self):
        self.rgba = self.hsv2rgb(self.hue,self.saturation,self.lightness,self.alpha)

    def hsv2rgb(self,h_or_color: Union[tuple, int], s: int = 0, v: int = 0, a: int = None) -> tuple:

        if type(h_or_color).__name__ == "tuple":
            if len(h_or_color) == 4:
                h, s, v, a = h_or_color
            else:
                h, s, v = h_or_color
        else: h = h_or_color
        r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100.0, v / 100.0)
        if a is not None: return r * 255, g * 255, b * 255, a
        return r * 255, g * 255, b * 255
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.color_indicator.setText("")
        self.black_ring.setText("")
    # retranslateUi



# import sys
# from PySide6.QtWidgets import QApplication,QMainWindow
# class MyMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(200, 200, 300, 600)

#         # Add a button to open the color picker
#         color_picker_button = QPushButton('Open Color Picker', self)
#         color_picker_button.clicked.connect(self.show_color_picker)
#         color_picker_button.move(50, 50)

#         # Add a button to quit the application
#         quit_button = QPushButton('Quit', self)
#         quit_button.clicked.connect(QApplication.instance().quit)
#         quit_button.move(50, 100)

#     def show_color_picker(self):
#         color_picker = ColorPicker(self)
#         if color_picker.exec_() == ColorPicker.Accepted:
#             selected_color = color_picker.rgba
#             print("Selected Color:", selected_color)

# def main():
#     app = QApplication(sys.argv)
#     window = MyMainWindow()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()