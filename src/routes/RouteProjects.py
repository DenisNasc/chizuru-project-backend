from flask_restful import Resource, marshal_with, reqparse, fields

from models.ModelProjects import create_projects_model

resource_fields = {'id': fields.Integer, 'name': fields.String}

projects_post_args = reqparse.RequestParser()
projects_post_args.add_argument("name",
                                type=str,
                                required=True,
                                help="Name is required")


def create_route_projects(db):
    ModelProjects = create_projects_model(db)

    class RouteProjects(Resource):
        @marshal_with(resource_fields)
        def get(self, user_id, project_id):
            try:
                result = ModelProjects.query.filter_by(id=project_id).first()
                return result
            except:
                return {}, 500

        @marshal_with(resource_fields)
        def post(self, user_id, project_id):
            args = projects_post_args.parse_args()

            try:
                already_exists = ModelProjects.query.filter_by(
                    name=args['name']).first()

                if already_exists: return {}, 409
                new_project = ModelProjects(name=args['name'])

                db.session.add(new_project)
                db.session.commit()

                return new_project, 201
            except:
                return {}, 500

    return RouteProjects