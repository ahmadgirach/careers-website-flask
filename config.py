import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_cors import CORS
from flask_migrate import Migrate

from dotenv import load_dotenv


load_dotenv()

class Base(DeclarativeBase):
  pass


ENVIRONMENT = os.getenv("ENVIRONMENT")
DATABASE_URL = os.getenv("DATABASE_URL")

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL if ENVIRONMENT == "prod" else "sqlite:///careers.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db.init_app(app)

migrate = Migrate(app, db)
