from dotenv import load_dotenv
load_dotenv()

# DB Config
DB_FILE = 'app/app.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

