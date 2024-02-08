import sys
from pathlib import Path
import json
import os
import utils

class ConfigManager:
    AppName = "CHASIKI"
    default_name = "default.json"

    def __init__(self):
        self.RootPath = self.getRootPath()
        self.configsList = None
        
        self.MainConfig = self.loadMainConfig()
        self.start_up_config = self.MainConfig.get('start_up_config')

        self.Config = None
        self.loadConfig()
        
    def loadConfig(self):
        RootPath = self.RootPath
        configName = self.start_up_config
        config_file = RootPath / configName
        if config_file.exists():
            with open(config_file, 'r') as f:
                s = json.load(f)
                self.Config = s
        else:
            if configName == self.default_name:
                self.saveConfig(self.default_name)
            else:
                self.setStartUpConfig(self.default_name)
            self.loadConfig()

    def deleteConfig(self,configName):
        rootPath = self.RootPath
        config_file = rootPath / configName
        if config_file.exists():
            config_file.unlink()

    def saveConfig(self, configName, configData=None):
        rootPath = self.RootPath
        if configData is None:
            # Default settings
            configData = {
                "start_hour": 5,
                "end_hour": 22,
                "progress_bar_color": [0, 128, 255],
                "window_corner_radius": 0,
                "outline_width": 2,
                "outline_color": [255, 255, 255],
                "bg_color": [0, 0, 0, 51]
            }

        config_file = rootPath / configName
        with open(config_file, 'w') as f:
            json.dump(configData, f)

    def createMainConfig(self):
        main_config_data = {"start_up_config": self.default_name}
        self.saveConfig("config.json", main_config_data)

    def loadMainConfig(self):
        rootPath = self.RootPath
        main_config_file = rootPath / "config.json"
        if main_config_file.exists():
            with open(main_config_file, 'r') as f:
                return json.load(f)
        else:
            self.createMainConfig()
            return self.loadMainConfig()
        
    def setStartUpConfig(self, start_up_config):
        rootPath = self.RootPath
        self.start_up_config = start_up_config
        self.MainConfig['start_up_config'] = start_up_config
        with open(rootPath / "config.json", 'w') as f:
            json.dump(self.MainConfig, f, indent=4)
        
    

    def getConfigsList(self):
        return [f.name for f in self.RootPath.iterdir() if f.is_file() and f.suffix == '.json' and f.name != 'config.json']

    # def getRootPath(self):
    #     if sys.platform == "win32":
    #         config_dir = Path.home() / "AppData" / "Roaming" / self.AppName
    #     elif sys.platform == "darwin":
    #         config_dir = Path.home() / "Library" / "Application Support" / self.AppName
    #     else:
    #         config_dir = Path.home() / ".config" / self.AppName

    #     config_dir.mkdir(parents=True, exist_ok=True)
    #     return config_dir
    def getRootPath(self):
        # Путь изменен на местоположение программы
        program_location = Path(__file__).resolve().parent / "configs"

        program_location.mkdir(parents=True, exist_ok=True)
        return program_location