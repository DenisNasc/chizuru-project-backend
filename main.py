from os import getenv

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from src import BASE_DIR

# ROUTES
from src.routes.RouteUsers import create_route_users
from src.routes.RouteProjects import create_route_projects


def main():
    IS_DEVELOPMENT = getenv('IS_DEVELOPMENT')
    print(getenv('Environment'))
    if IS_DEVELOPMENT:
        DEVELOPMENT_DATABASE_URI = getenv('DEVELOPMENT_DATABASE_URI')
        DATABASE_URI = f'sqlite:///{BASE_DIR}/{DEVELOPMENT_DATABASE_URI}'

    else:
        DATABASE_URI = BASE_DIR + getenv('PRODUCTION_DATABASE_URI')

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

    api = Api(app)
    db = SQLAlchemy(app=app)

    api.add_resource(create_route_users(db), "/users/<string:user_id>")
    api.add_resource(create_route_projects(db),
                     "/users/<string:user_id>/projects/<string:project_id>")

    db.create_all()  # VERIFICAR COMO MANIPULAR AS TABELAS DO BANCO DE DADOS
    app.run(debug=IS_DEVELOPMENT)


if __name__ == "__main__":
    main()
