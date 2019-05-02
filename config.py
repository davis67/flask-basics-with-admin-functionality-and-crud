class Config(object):
    """
    Common configurations
    """

    #put any configurations here that are common accross all environments
    SECRET_KEY = 'p9B<Eid9%$101'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@1projects@localhost/flask_crud'
    

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
        'development':DevelopmentConfig,
        'production':ProductionConfig
    }