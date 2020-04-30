DEBUG = True

SECRET_KEY = 'insecurekeyfordev'

#SQLAlchemy
db_uri = 'postgresql://postgres:password@localhost/CoinLogic'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
