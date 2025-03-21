import json
import os

class Config:
    def __init__(self):
        if not os.path.exists("config.json"):
            with open("config.json", "w") as f:
                config = {
                            "base_url": "your_base_url",
                            "api_key": "your_api_key",
                            "model": "your_model",
                        }
                f.write(json.dumps(config))
                print("config.json created. Please fill in the details or use commendline to set them")
        with open("config.json", "r") as f:
            self.config = json.load(f)

    def set_model(self, model):
        self.config["model"] = model
        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)

    def set_base_url(self, base_url):
        self.config["base_url"] = base_url
        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)

    def set_api_key(self, api_key):
        self.config["api_key"] = api_key
        with open("config.json", "w") as f:
            json.dump(self.config, f, indent=4)

    def get_config(self):
        return self.config

global_config = Config()