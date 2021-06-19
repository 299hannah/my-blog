import os

class Config:
    """
    General parent class

    """
    SECRETE_KEY = os.environ.get('SECRETE_KEY') or 's3cr3t3k3y'

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
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig,

    'default': DevConfig
}
