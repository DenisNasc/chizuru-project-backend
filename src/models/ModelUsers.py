from datetime import datetime


def create_users_model(db):
    class ModelUsers(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(30), nullable=False)
        email = db.Column(db.String(60), nullable=False)
        encrypted_password = db.Column(db.String(72), nullable=False)
        is_verified = db.Column(db.Boolean(), default=False)
        is_admin = db.Column(db.Boolean(), default=False)
        updated_at = db.Column(db.DateTime, default=datetime.now)
        created_at = db.Column(db.DateTime, default=datetime.now)

        def __repr__(self) -> str:
            return f"User -> name = {self.name}; email = {self.email}"

    return ModelUsers