import os
from urllib.parse import quote_plus
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'tuannd72storage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'iCiuw3Pwr6W7PgTLH4xcHts6djqCntagMs+nsF5U2ChiW7utVkZYd2hLT46Cd2jKKNm78Fw7oBae+ASthGQGww=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'mycontainer'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'tuannd72-sql.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'tuannd72-cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'tuannd72admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Tt@123456'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
   # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
   # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{SQL_USER_NAME}:{quote_plus(SQL_PASSWORD)}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "ENTER_CLIENT_ID_HERE"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session