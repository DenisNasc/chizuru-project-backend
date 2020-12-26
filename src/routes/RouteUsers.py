from flask_restful import Resource, marshal_with, reqparse, fields

from src.models.ModelUsers import create_users_model

# SERIALIZANDO OS DADOS DO BANCO DE DADOS
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'encrypted_password': fields.String
}

# DEFININDOS OS CAMPOS DO BODY DA REQUEST
users_post_args = reqparse.RequestParser()
users_post_args.add_argument("name",
                             type=str,
                             required=True,
                             help="Name is required")
users_post_args.add_argument("email",
                             type=str,
                             required=True,
                             help="Email is required")
users_post_args.add_argument("encrypted_password",
                             type=str,
                             required=True,
                             help="Encrypted Password is required")


def create_route_users(db):
    ModelUsers = create_users_model(db)

    class RouteUsers(Resource):
        @marshal_with(resource_fields)
        def get(self, user_id):
            try:
                result = ModelUsers.query.filter_by(id=user_id).first()

                if not result: return {}, 404
                return result

            except:
                return {}, 500

        @marshal_with(resource_fields)
        def post(self, user_id):
            args = users_post_args.parse_args()

            try:
                already_exists = ModelUsers.query.filter_by(
                    email=args['email']).first()

                if already_exists:
                    return {}, 409

                new_user = ModelUsers(
                    name=args['name'],
                    email=args['email'],
                    encrypted_password=args['encrypted_password'])

                db.session.add(new_user)
                db.session.commit()
                return new_user, 201
            except:
                return {}, 500

        # def delete(self, user_id):
        #     del videos[user_id]
        #     return '', 204

    return RouteUsers