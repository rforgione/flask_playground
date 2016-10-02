from app import db

class Models_Names(db.Model):
    def __init__(self):
        pass

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
