#this file is the configration file for our web application(app), and the app 
#have the method app.config.from_object(config class), the file name config.py
#is fixed.we can have many different config in different envirouments.

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEATDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    SECRET_KEY = "hard string to guess"
    
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "1367695045@qq.com"
    MAIL_PASSWORD = "qdxifurkfcxtghaf"
    DOIT_MAIL_SUBJECT_PREFIX = "[DOIT.Team]"
    DOIT_MAIL_SENDER = "DOIT.Team<1367695045@qq.com>"
    DOIT_ADMIN = "1367695045@qq.com"
    
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    pass
    
class TestConfig(Config):
    pass
# Dictionary used in app.__init__.py to configure 
#our application in different envirnoment.
config = {
'default' : Config,
'development' : DevelopmentConfig,
'test' : TestConfig
}