import requests
import yaml
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(asctime)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M")

def FacebookCleaner():
  APP_ID = None
  SECRET = None
  SHORT_TOKEN = None

  with open("private/config.yaml", "r") as config_file:
    config_yaml = yaml.load(config_file, Loader=yaml.SafeLoader)

    APP_ID = config_yaml["app_id"]
    SECRET = config_yaml["secret"]
    SHORT_TOKEN = config_yaml["app_id"]

  logging.debug(APP_ID)



if __name__=="__main__":
  FacebookCleaner()
