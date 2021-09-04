import os
from decouple import config

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'Database/db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
