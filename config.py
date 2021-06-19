import os

class Config:
    """
    General parent class

    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cr3t3k3y'

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
    QUOTE_API_BASE_URL="http://quotes.stormconsultancy.co.uk/{}/{}"
    QUOTE_API_KEY = os.environ.get('QUOTE_API_KEY')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cr3t3k3y'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig,

    'default': DevConfig
}
