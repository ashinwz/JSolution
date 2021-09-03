import os


class Config(object):
    basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    SECRET_KEY = 'S#perS3crEt_007'

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
