"""Load configuration data from the environment."""
import os


def load_config():
    return {
        'log_level': os.environ.get('LOG_LEVEL', 'debug').upper(),
    }
