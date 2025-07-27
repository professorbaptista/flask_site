
# from flask import Flask
# from models.models import db

# def criar_banco():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/site.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)

#     with app.app_context():
#         db.create_all()
#         print('Banco de dados criado com sucesso.')

# if __name__ == "__main__":
#     criar_banco()
