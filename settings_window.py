from PySide6.QtWidgets import QDialog,QSizePolicy, QLineEdit,QComboBox,QLabel,QSpacerItem ,QSpinBox, QSlider, QPushButton, QVBoxLayout, QColorDialog, QFrame, QHBoxLayout
from PySide6.QtGui import QColor, Qt,QIcon, QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
import widgets.periodSelector as periodSelector
import widgets.filenameDialog as filenameDialog
import widgets.deleteConfirmation as deleteConfirmation
import utils, os, stylize
from widgets.colorPicker import ColorPicker as ColorPicker

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        script_path = os.path.abspath(__file__)
        self.script_directory = os.path.dirname(script_path)
        self.popup_dialog = None
        self.setWindowTitle("Settings")
        self.setMaximumSize(300, 300)
        self.config = self.parent().config
        # Widgets
        self.pg_color_label = QLabel("Pick color of:")
        self.pg_color_button = QPushButton("Fill")
        self.outline_pg_color_button = QPushButton("Outline")
        self.bg_pg_button = QPushButton("BackGr")
        self.corner_radius = QSlider(Qt.Horizontal)
        self.border_width = QSlider(Qt.Horizontal)
        self.separator = QFrame()
        self.period = periodSelector.PeriodSelector()

        self.rename_config_button = QPushButton()
        self.create_config_button = QPushButton()
        self.delete_config_button = QPushButton()
        self.save_config_button = QPushButton()

        self.config_selector = QComboBox()

        # Layouts
        self.layout = QVBoxLayout(self)
        self.buttons_vstack = QVBoxLayout()
        self.period_colors_stack = QHBoxLayout()
        self.config_layout = QHBoxLayout()

        # Setup UI
        self.setStyleSheet("background-color: #232323; color: white;")
        self.setup_ui()

    def setup_ui(self):
        # Period Selector
        self.config_setup()
        self.period_setup()
        self.period_colors_stack.addWidget(self.period)
        self.period_colors_stack.addLayout(self.buttons_vstack)

        # Color Buttons
        self.color_buttons_setup()
        self.layout.addLayout(self.period_colors_stack)
        # Slider
        self.corner_radius_setup()
        self.border_width_setup()

        # Separator
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

    def period_setup(self):
        self.period.selected_period = ((self.parent().start_hour, self.parent().end_hour))
        self.period.pb_color = self.parent().progress_bar_color
        self.period.radius = 55
        self.period.second_radius = 15
        self.period.border_width = self.parent().outline_width
        self.period.border_color = self.parent().outline_color
        self.period.bg_color = self.parent().bg_color
        self.period.periodChanged.connect(self.saveSettings)

    def config_setup(self):
        stylize.custom_btn(self.create_config_button)
        stylize.custom_btn(self.rename_config_button)
        stylize.custom_btn(self.delete_config_button)
        stylize.custom_btn(self.save_config_button)
        stylize.custom_combo_box(self.config_selector)

        self.rename_config_button.clicked.connect(self.rename_config_clicked)
        self.create_config_button.clicked.connect(self.create_config_clicked)
        self.delete_config_button.clicked.connect(self.delete_config_clicked)
        self.save_config_button.clicked.connect(self.save_config_clicked)

        self.create_config_button.setToolTip("new config")
        self.rename_config_button.setToolTip("rename")
        self.delete_config_button.setToolTip("delete")
        self.save_config_button.setToolTip("save")

        self.UpdateItems_config_selector()
        self.config_selector.activated.connect(self.ConfigSelected)

        self.config_selector.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.create_config_button.setIcon(QIcon(self.script_directory +"/icons/create.png"))
        self.rename_config_button.setIcon(QIcon(self.script_directory +"/icons/rename.png"))
        self.delete_config_button.setIcon(QIcon(self.script_directory +"/icons/delete.png"))
        self.save_config_button.setIcon(QIcon(self.script_directory +"/icons/save.png"))
        utils.add_widgets_to_layout(self.config_layout,[self.create_config_button,
                                                       self.config_selector,
                                                       self.rename_config_button,
                                                       self.delete_config_button,
                                                       self.save_config_button])
        self.config_layout.setSpacing(5)
        self.layout.addLayout(self.config_layout)

    def color_buttons_setup(self):
        self.color_buttons_setup_visual()
        self.pg_color_button.clicked.connect(self.pg_color_button_clicked)
        self.outline_pg_color_button.clicked.connect(self.outline_pg_color_button_clicked)
        self.bg_pg_button.clicked.connect(self.bg_pg_button_clicked)
        self.buttons_vstack.setSpacing(5)
        utils.add_widgets_to_layout(self.buttons_vstack,[self.pg_color_label,
                                                        self.pg_color_button,
                                                        self.outline_pg_color_button,
                                                        self.bg_pg_button])
        self.buttons_vstack.setAlignment(Qt.AlignCenter)
    
    def color_buttons_setup_visual(self):
        stylize.color_button(self.pg_color_button,self.parent().progress_bar_color)
        stylize.color_button(self.outline_pg_color_button,self.parent().outline_color)
        stylize.color_button(self.bg_pg_button,self.parent().bg_color)

    def corner_radius_setup(self):
        self.corner_radius.setMinimum(1)
        self.corner_radius.setMaximum(10)
        self.corner_radius.setSingleStep(1) 
        self.corner_radius.setValue(self.parent().window_corner_radius)
        self.corner_radius.valueChanged.connect(self.saveSettings)
        stylize.slider_style(self.corner_radius,utils.QColor2Array(self.parent().progress_bar_color))
        self.layout.addWidget(QLabel("Corner radius:"))
        self.layout.addWidget(self.corner_radius)

    def border_width_setup(self):
        self.border_width.setMinimum(0)
        self.border_width.setMaximum(3)
        self.border_width.setSingleStep(1) 
        self.border_width.setValue(self.parent().outline_width)
        self.border_width.valueChanged.connect(self.saveSettings)
        stylize.slider_style(self.border_width,utils.QColor2Array(self.parent().progress_bar_color))
        self.layout.addWidget(QLabel("Border width:"))
        self.layout.addWidget(self.border_width)

    def pg_color_button_clicked(self):
        self.showColorDialog(self.parent().progress_bar_color, self.pg_color_button)
        self.saveSettings()

    def outline_pg_color_button_clicked(self):
        self.showColorDialog(self.parent().outline_color, self.outline_pg_color_button)
        self.saveSettings()
    
    def bg_pg_button_clicked(self):
        self.showColorDialog(self.parent().bg_color, self.bg_pg_button)
        self.saveSettings()

    def showColorDialog(self, color_var: QColor, button):
        old_color = color_var.getHsv()
        old_color = list(color_var.getHsv())
        old_color[1] = (old_color[1]/255*100)
        old_color[2] = (old_color[2]/255*100)
        print(old_color)
        color_dialog = ColorPicker(self, old_color[0], old_color[1], old_color[2], old_color[3])
        if color_dialog.exec_():
            color = color_dialog.rgba
            color = utils.Array2QColor(color)
            color_var.setRgb(color.red(), color.green(), color.blue(),color.alpha())
            stylize.color_button(button,color)
            if button.text() == "Fill":
                self.period.pb_color = color_var
            elif button.text() == "Outline":
                self.period.border_color = color_var
            elif button.text() == "BackGr":
                self.period.bg_color = color_var
            self.customUpdate()
            self.period.update()
    # def showColorDialog(self, color_var, button):
    #     color_dialog = QColorDialog(self)
    #     if color_dialog.exec_():
    #         color = color_dialog.currentColor()
    #         color_var.setRgb(color.red(), color.green(), color.blue(),color.alpha())
    #         stylize.color_button(button,color)
    #         if button.text() == "Fill":
    #             self.period.pb_color = color_var
    #         elif button.text() == "Outline":
    #             self.period.border_color = color_var
    #         elif button.text() == "BackGr":
    #             self.period.bg_color = color_var
    #         self.customUpdate()
    #         self.period.update()

    def saveSettings(self):
        start_hour = self.period.selected_period[0]
        end_hour = self.period.selected_period[1]
        border = self.border_width.value()
        window_corner_radius = self.corner_radius.value()
        progress_bar_color = self.parent().progress_bar_color
        outline_progress_bar_color = self.parent().outline_color
        bg_color = self.parent().bg_color

        self.parent().updateSettings(start_hour, end_hour, window_corner_radius, progress_bar_color, outline_progress_bar_color,border,bg_color)
    
    def save_config_clicked(self):
        self.config.saveConfig(self.config.start_up_config,self.config.Config)

    def create_config_clicked(self):
        if not self.popup_dialog:
            self.popup_dialog = filenameDialog.PopupDialog(self)
        if self.popup_dialog.exec_():
            c = self.popup_dialog.text_field.text()
            self.config.saveConfig(c+".json")
            self.UpdateItems_config_selector()
            self.popup_dialog = None

    def rename_config_clicked(self):
        if self.config.start_up_config != "default.json":
            self.popup_dialog = filenameDialog.PopupDialog(self)
            self.popup_dialog.text_field.setText(self.config.start_up_config[:-5])
            if self.popup_dialog.exec_():
                c = self.popup_dialog.text_field.text()
                self.config.saveConfig(c+".json",self.config.Config)
                self.config.deleteConfig(self.config.start_up_config)
                self.config.setStartUpConfig(c+".json")
                self.UpdateItems_config_selector()
                self.popup_dialog = None
                # Your logic to handle rename using 'c'

    def delete_config_clicked(self):
        if self.config.start_up_config != "default.json":
            confirmation_dialog = deleteConfirmation.ConfirmationDialog(self)
            result = confirmation_dialog.exec_()
            if result == QDialog.Accepted:
                self.config.deleteConfig(self.config.start_up_config)
                self.config.setStartUpConfig("default.json")
                self.UpdateItems_config_selector()
                self.config.loadConfig()
                self.parent().readConfigProperties()
                self.customUpdate()

    def ConfigSelected(self):
        self.config.setStartUpConfig(self.config_selector.currentText()+".json")
        self.config.loadConfig()
        self.parent().readConfigProperties()
        self.customUpdate()

    def UpdateItems_config_selector(self):
        configs_list = self.parent().config.getConfigsList()
        current_items = [self.config_selector.itemText(i) for i in range(self.config_selector.count())]

        # Добавляем новые элементы
        for config in configs_list:
            config_name = config[:-5]
            if config_name not in current_items:
                self.config_selector.addItem(config_name)

        # Удаляем старые элементы
        for i in range(self.config_selector.count()):
            item_text = self.config_selector.itemText(i)
            if item_text not in [config[:-5] for config in configs_list]:
                self.config_selector.removeItem(i)
                break

        # Устанавливаем текущий индекс на основе self.config.start_up_config
        initial_text = self.config.start_up_config[:-5]
        initial_index = self.config_selector.findText(initial_text)
        if initial_index != -1:
            self.config_selector.setCurrentIndex(initial_index)

    def customUpdate(self):
        #period update
        self.period_setup()
        self.color_buttons_setup_visual()
        stylize.slider_style(self.border_width,utils.QColor2Array(self.parent().progress_bar_color))
        stylize.slider_style(self.corner_radius,utils.QColor2Array(self.parent().progress_bar_color))
        self.update()
    
    def drawIcon(self,iconPath):
        svg_renderer = QSvgRenderer(iconPath)
        pixmap = QPixmap(svg_renderer.defaultSize())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()
        return QIcon(pixmap)