

from requests import HTTPError

import requests
import yaml
import logging
import json

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(asctime)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M")

HOST = "https://graph.facebook.com/"

def FacebookCleaner():

  with open("private/config.yaml", "r") as config_file:
    config_yaml = yaml.load(config_file, Loader=yaml.SafeLoader)


  field_param = {"fields": "id,name,posts{object_id,parent_id,id,message,admin_creator,width,sharedposts,story,status_type,via,properties,permalink_url,message_tags,link,description,caption,type}"}
  
  logging.debug(request(config_yaml, field_param))
  
  


def request(config, url_params={}):
  """Wrapper for sending GET to Facebook.
  
  Args:
    config: YAML object of config file.
    url_params: Dictionary of parameters to add to GET. 

  Returns:
    HTTP response or error. 
  """
  host = HOST + f"/{config['user_id']}/"
  params = {"fields": "id,name",
            "access_token": config['user_token']}

  params.update(url_params)

  try: 
    response = requests.get(host, params=params)
    logging.info(f"Sending to Facebook: {response.status_code}")

    response.encoding = "utf-8"
    return json.dumps(response.text, indent=4)

  except HTTPError as e:
    return e





if __name__=="__main__":
  FacebookCleaner()
