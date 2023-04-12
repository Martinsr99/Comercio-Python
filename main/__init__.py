import os
from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api
#Importo el modulo para crear la apirest
from flask_restful import Api
#Importo el modulo para conectarme con una base de datos SQL
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    #Cargo las variables de entorno
    load_dotenv()

    #Configuracion de la base de datos SQL
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}', os.O_CREAT)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)

    import main.resources as resources
    api.add_resource(resources.ClientesResource,'/clientes')
    api.add_resource(resources.ClienteResource,'/clientes/<id>')

    api.init_app(app)

    return app