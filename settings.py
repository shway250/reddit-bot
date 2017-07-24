# settings.py
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


FOO = os.environ.get("FOO")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")