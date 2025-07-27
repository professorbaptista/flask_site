
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# db = SQLAlchemy()

# class Contacto(db.Model):
#     __tablename__ = 'contactos'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     message = db.Column(db.Text, nullable=False)
#     data = db.Column(db.DateTime, default=datetime.now(datetime.utcnow))

# class Depoimento(db.Model):
#     __tablename__ = 'depoimentos'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     message = db.Column(db.Text, nullable=False)
#     data = db.Column(db.DateTime, default=datetime.utcnow)
