from src.extentions import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    long = db.Column(db.String, index=True)
    short = db.Column(db.String, unique=True, index=True)
    total_clicks = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f'<URL {self.id}: {self.short}'
