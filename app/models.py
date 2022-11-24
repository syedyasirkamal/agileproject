from flask_sqlalchemy import SQLAlchemy
from flask import g, current_app
from flask_sqlalchemy import SQLAlchemy

db = None
def get_db():
  global db
  if not db:
    db = SQLAlchemy(current_app)
  return db
