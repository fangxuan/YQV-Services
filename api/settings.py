import os

os_env = os.environ

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'admingyu'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'YQV_APP'

REDIS_HOST = '127.0.0.1'
REDIS_POST = '6379'


class Config(object):
    SECRET_KEY = os_env.get('API_SECRET', 'sf347fr7g8dfhjg9q34j09*4598-q3+q902kdsvmz#cklbvmna90235q0349jrga')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    UPLOAD_FOLDER = '/static'
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'redis'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(user=MYSQL_USER,
                                                                                                  password=MYSQL_PASSWORD,
                                                                                                  host=MYSQL_HOST,
                                                                                                  port=MYSQL_PORT,
                                                                                                  database=MYSQL_DATABASE)
    SQLALCHEMY_BINDS = {'vnapp': 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(user=MYSQL_USER,
                                                                                                     password=MYSQL_PASSWORD,
                                                                                                     host=MYSQL_HOST,
                                                                                                     port=MYSQL_PORT,
                                                                                                     database=MYSQL_DATABASE)}
    ASSETS_DEBUG = True
    CACHE_TYPE = 'redis'
