import json
import os
import sys
from pathlib import Path

class Config:
    def __init__(self):
        self.config_path = Path(sys.executable).parent + "/config.json"
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w") as f:
                config = {
                            "base_url": "your_base_url",
                            "api_key": "your_api_key",
                            "model": "your_model",
                        }
                f.write(json.dumps(config))
                print("config.json created. Please fill in the details or use commendline to set them")
        with open(self.config_path, "r") as f:
            self.config = json.load(f)

    def set_model(self, model):
        self.config["model"] = model
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def set_base_url(self, base_url):
        self.config["base_url"] = base_url
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def set_api_key(self, api_key):
        self.config["api_key"] = api_key
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def get_config(self):
        return self.config

global_config = Config()