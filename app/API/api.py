from flask import jsonify, Blueprint
from app.DataAccess.Models import FirstNames, LastNames, User
from app import db

api_bp = Blueprint(
    'api_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@api_bp.route('/get-persons/<int:amount>')
def get_persons(amount):
    firstnames = FirstNames.get_multiple(amount)
    lastnames = LastNames.get_multiple(amount)
    res = list()
    for x, y in zip(firstnames, lastnames):
        res.append({
            'firstname': x.name,
            'lastname': y.name
        })

    return jsonify(res)

@api_bp.route('/get-person')
def get_person():
    firstname = FirstNames.get_single()
    lastname = LastNames.get_single()
    res = {
        'firstname':firstname.name,
        'lastname':lastname.name
    }
    return jsonify(res)

@api_bp.route('/get-CPR')
def get_cpr():

    return 'firstnames.name'

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
