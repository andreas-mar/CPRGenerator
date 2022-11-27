from flask import jsonify, Blueprint
from app.DataAccess.Models import FirstNames, LastNames, User
from app import db
from app.BusinessLogic.FictionalPerson import FictionalPerson
from app.BusinessLogic.CPRGenerator import CPRGenerator
import datetime as dt

api_bp = Blueprint(
    'api_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@api_bp.route('/get-persons/<int:amount>')
def get_persons(amount):
    if amount > 100:
        return 'Request too high', 400
    start = dt.datetime.now() - dt.timedelta(days=365 * 100)
    end = dt.datetime.now() - dt.timedelta(days=365 * 18)
    res = list()
    for i in range(amount):
        firstname = FirstNames.get_single_firstname()
        lastname = LastNames.get_single_lastname()
        p = FictionalPerson(lastname.name, start, end)
        p.first_name = firstname.name
        res.append(p.to_dict())

    return jsonify(res)

@api_bp.route('/get-person')
def get_person():
    firstname = FirstNames.get_single_firstname()
    lastname = LastNames.get_single_lastname()
    res = FictionalPerson(firstname.name, lastname.name, 'Male').to_dict()
    return jsonify(res)

@api_bp.route('/validate-cpr/<string:cpr>')
def validate_cpr(cpr):
    return jsonify({'valid': str(CPRGenerator().validate_CPR(cpr))})

@api_bp.route('/init')
def init_app():
    new_user = User(username='andreas', password='test')
    db.session.add(new_user)
    db.session.commit()
    return 'true'

@api_bp.route('/see-user')
def user():
    user = User.query.first()
    return jsonify(user.to_dict())
