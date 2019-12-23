from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///localhost.sqlite")

class User (db.Model):
    uid = db.Column(db.Integer, primary_key=True)

  #Login information
    email = db.Column (db.String, unique=True)
    password = db.Column(db.String)
    token = db.Column(db.Integer)

    #Additional info
    name = db.Column(db.String)

    #For game playing
    secret_number = db.Column(db.Integer)