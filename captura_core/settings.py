import os, sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


class BaseConfig:
    captura_ADMIN_EMAIL = os.getenv('captura_ADMIN', 'admin@helloflask.com')
    captura_PHOTO_PER_PAGE = 12
    captura_COMMENT_PER_PAGE = 15
    captura_NOTIFICATION_PER_PAGE = 20
    captura_USER_PER_PAGE = 20
    captura_MANAGE_PHOTO_PER_PAGE = 20
    captura_MANAGE_USER_PER_PAGE = 30
    captura_MANAGE_TAG_PER_PAGE = 50
    captura_MANAGE_COMMENT_PER_PAGE = 30
    captura_SEARCH_RESULT_PER_PAGE = 20
    captura_MAIL_SUBJECT_PREFIX = '[captura]'
    captura_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    captura_PHOTO_SIZE = {'small': 400,
                         'medium': 800}
    captura_PHOTO_SUFFIX = {
        captura_PHOTO_SIZE['small']: '_s',  # thumbnail
        captura_PHOTO_SIZE['medium']: '_m',  # display
    }

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024  # file size exceed to 3 Mb will return a 413 error response.

    BOOTSTRAP_SERVE_LOCAL = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AVATARS_SAVE_PATH = os.path.join(captura_UPLOAD_PATH, 'avatars')
    AVATARS_SIZE_TUPLE = (30, 100, 200)

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('captura Admin', MAIL_USERNAME)

    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    DROPZONE_ENABLE_CSRF = True

    WHOOSHEE_MIN_STRING_LEN = 1


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'data-dev.db')
    REDIS_URL = "redis://localhost"


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
