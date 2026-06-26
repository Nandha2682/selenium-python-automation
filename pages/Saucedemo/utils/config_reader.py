import configparser
import os

config = configparser.ConfigParser()

current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, "..", "config", "config.ini")
config_path = os.path.abspath(config_path)

print("CONFIG PATH:", config_path)

config.read(config_path)

print("SECTIONS:", config.sections())
print("DEFAULTS:", dict(config.defaults()))

def get_config(key):
    return config.get("DEFAULT", key)