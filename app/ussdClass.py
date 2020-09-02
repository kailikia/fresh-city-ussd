from config import db
from sqlalchemy.sql import func

class USSDModel(db.Model):
    __tablename__ = 'ussds'
    id = db.Column(db.Integer(), primary_key=True)
    sessionID = db.Column(db.String(120), nullable=False)
    phoneNumber = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    county = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    products = db.Column(db.String(), nullable=False)
    ready = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.String(120), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # CREATE
    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_all(cls):
        return cls.query.order_by(cls.time_created.desc()).all()

class Phone(db.Model):
    __tablename__ = 'unique_phones'
    id = db.Column(db.Integer(), primary_key=True)
    sessionID = db.Column(db.String(120), nullable=False)
    phoneNumber = db.Column(db.String(120), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # CREATE
    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_all(cls):
        return cls.query.order_by(cls.time_created.desc()).all()

    @classmethod
    def fetch_one(cls,id):
        rec=cls.query.filter_by(sessionID = id).first()
        if rec:
            return True
        else:
            return False
        
class LoggedSession():
    loggedIn = False

    def set_session(self, value):
        self.loggedIn = value

    def get_session(self):
        return self.loggedIn
