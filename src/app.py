import os
from IndexRunner.EventUtils import kafka_watcher
from configparser import ConfigParser
import time
import logging
from threading import Thread

from src.load_config import load_config

config = load_config()

# create logger
logger = logging.getLogger('indexrunner')
logger.setLevel(config['log_level'])

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(config['log_level'])
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if not os.environ.get('KB_DEPLOYMENT_CONFIG'):
    raise RuntimeError('KB_DEPLOYMENT_CONFIG environment variable should be set to a valid path.')

config_file = os.environ['KB_DEPLOYMENT_CONFIG']
config = ConfigParser()
config.read(config_file)
cfg = dict()
for (name, val) in config.items('IndexRunner'):
    cfg[name] = val

kafka_thread = Thread(target=kafka_watcher, args=[cfg])
kafka_thread.daemon = True
kafka_thread.start()
while True:
    time.sleep(600)
