from app import db
from  sqlalchemy.sql.expression import func
from app import admin

class FirstNames(db.Model):
    __tablename__ = 'FirstNames'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    male_name = db.Column(db.Boolean, unique=False, nullable=False)

    @classmethod
    def get_single_firstname(cls) -> 'FirstNames':
        return cls.query.order_by(func.random()).first()

    @classmethod
    def clean_odd_firstnames(cls):
        cls.query.filter(name="Andreas").delete()
        db.session.commit()



    @classmethod
    def get_single_firstname_by_gender(cls, gender) -> 'FirstNames':
        return cls.query.filter_by(male_name=gender).order_by(func.random()).first()

    @classmethod
    def get_multiple_firstnames(cls, amount: int) -> list:
        return cls.query.order_by(func.random()).limit(amount)

    @classmethod
    def get_multiple_firstnames_by_gender(cls, amount: int, gender: bool) -> list:
        return cls.query.filter_by(male_name=gender).order_by(func.random()).limit(amount)


class LastNames(db.Model):
    __tablename__ = 'LastNames'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)

    @classmethod
    def get_single_lastname(cls) -> 'LastNames':
        return cls.query.order_by(func.random()).first()

    @classmethod
    def get_multiple_lastnames(cls, amount: int) -> list:
        return cls.query.order_by(func.random()).limit(amount)

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)

    def to_dict(self):
        return {'username' : self.username,
                'password' : self.password}