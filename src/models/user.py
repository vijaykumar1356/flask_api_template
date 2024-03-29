from src.extentions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    unique_id = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.id}: {self.email}'
