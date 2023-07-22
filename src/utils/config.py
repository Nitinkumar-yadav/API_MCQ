import configparser
import os


# here create class of config manager
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = configparser.ConfigParser()
            config_file = os.path.join("docs", "configs.yaml")
            cls._instance._config.read(config_file)
            #cls._instance['prompt']  #reading prompt
        return cls._instance
    
    def get_api_key(self):
        return self._config.get("OpenAI", "API_key")
    