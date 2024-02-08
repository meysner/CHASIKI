from PySide6.QtGui import QColor

def QColor2Array(Qcolor):
    return [Qcolor.red(),Qcolor.green(),Qcolor.blue(),Qcolor.alpha()]

def Array2QColor(arr):
    if len(arr)==3: 
        return QColor(int(arr[0]), int(arr[1]), int(arr[2]))
    elif len(arr)==4:  
        return QColor(int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]))
    
def getInvertTextColor(Qcolor):
    aver = (Qcolor.red()+Qcolor.blue()+Qcolor.green())/3
    if aver < 255/2:
        return "white"
    else:
        return "black"

def add_widgets_to_layout(layout, widgets):
    for widget in widgets:
        layout.addWidget(widget)

def rgba_to_hex(rgba):
    if len(rgba) != 4:
        raise ValueError("Массив RGBA должен содержать 4 элемента (R, G, B, A)")
    
    hex_r = format(rgba[0], '02X')
    hex_g = format(rgba[1], '02X')
    hex_b = format(rgba[2], '02X')
    
    hex_code = '#' + hex_r + hex_g + hex_b
    
    return hex_code

