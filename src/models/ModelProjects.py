from datetime import datetime


def create_projects_model(db):
    class ModelProjects(db.Model):
        __tablename__ = 'projects'
        id = db.Column(db.Integer, primary_key=True)
        # user_id = db.Column(db.Integer, ForeignKey('users.id'))
        name = db.Column(db.String(30), nullable=False)
        engineer = db.Column(db.String(30))
        shipyard = db.Column(db.String(30))
        updated_at = db.Column(db.DateTime, default=datetime.now)
        created_at = db.Column(db.DateTime, default=datetime.now)

        def __repr__(self) -> str:
            return f"User -> name = {self.name}; email = {self.email}"

    return ModelProjects