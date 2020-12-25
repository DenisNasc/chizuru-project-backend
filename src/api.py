from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import BaseQuery, SQLAlchemy

# ROUTES
from routes.RouteUsers import create_route_users
from routes.RouteProjects import create_route_projects

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

api = Api(app)
db = SQLAlchemy(app=app, query_class=BaseQuery)

api.add_resource(create_route_users(db), "/users/<string:user_id>")
api.add_resource(create_route_projects(db),
                 "/users/<string:user_id>/projects/<string:project_id>")

if __name__ == "__main__":
    db.create_all()  # VERIFICAR COMO MANIPULAR AS TABELAS DO BANCO DE DADOS
    app.run(debug=True)