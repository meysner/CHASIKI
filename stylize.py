import utils
from PySide6.QtGui import QColor
def custom_btn(button):
    button.setStyleSheet('''
        QPushButton {
            background-color: black;
            border: none; 
            color: white;
            padding: 6px 8px; 
            text-decoration: none; 
            font-size: 16px;
            border-radius:5px;
            
        }
        
        QPushButton:hover {
            background-color: #45a049;
        }
    ''')

def custom_combo_box(combo_box):
    combo_box.setStyleSheet('''
    QComboBox {
        background-color: black; 
        border: none; 
        color: white;
        padding: 6px 8px; 
        text-align: center; 
        text-decoration: none; 
        font-size: 16px;
        height: 16px;
        border-radius:5px;
    }
    
    QComboBox:hover {
        background-color: #45a049;
    }
''')    
    
def color_button(button,color):
    textColor = utils.getInvertTextColor(color)
    color = color.name()
    button.setStyleSheet(f'''
        QPushButton {{
            border: none; 
            color: {textColor};
            padding: 4px 0px; 
            text-decoration: none; 
            font-size: 12px;
            border-radius:5px;
            background-color: {color};
        }}
    ''')

def slider_style(slider, color):
    import utils
    color = utils.rgba_to_hex(color)
    slider.setStyleSheet(f"""
QSlider::groove:horizontal {{
    background-color: transparent;
    height: 10px;
}}

QSlider::sub-page:horizontal {{
    background-color: {color};
    border-radius:3px;
}}

QSlider::add-page:horizontal {{
    background-color: color;
    border-radius:3px;
}}

QSlider::handle:horizontal {{
    background-color: white;
    border: 1px solid #777;
    width: 20px;
    margin-top: -5px;
    margin-bottom: -5px;
    border-radius: 10px;
}}

QSlider::handle:horizontal:hover {{
    background-color: #ccc;
}}

QSlider::sub-page:horizontal:disabled {{
    background-color: #bbb;
}}

QSlider::add-page:horizontal:disabled {{
    background-color: #999;
}}

QSlider::handle:horizontal:disabled {{
    background-color: #888;
}}
""")
