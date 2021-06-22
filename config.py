import os

class Config:
    """
    General parent class

    """
    BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cr3t3k3y'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    """
    production configuration
    Arg:
        Config: The parent configuration class with general configuration settings

    """
    pass

class TestConfig(Config):
    """
    test configuration
    """
    pass

class DevConfig(Config):

    """
    Development Configuration
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/myblog'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig,

    'default': DevConfig
}
