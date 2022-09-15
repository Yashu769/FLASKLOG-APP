import os


class Config:
    # put confidential details using environment variables to hide them 
    SECRET_KEY = '929d00161065322d62b229385e66b225'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'yj9466371478@gmail.com'
    MAIL_PASSWORD = 'Jain@74046'