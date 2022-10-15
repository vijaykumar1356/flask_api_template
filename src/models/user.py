from src.extentions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    game_string = db.Column(db.String)

    def __repr__(self) -> str:
        return f'<User {self.id}: {self.first_name}'
