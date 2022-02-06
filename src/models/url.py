from src.extentions import db


class URL(db.model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    long = db.Column(db.String, unique=True, index=True)
    short = db.Column(db.String, unique=True, index=True)
    total_clicks = db.Column(db.Integer)
