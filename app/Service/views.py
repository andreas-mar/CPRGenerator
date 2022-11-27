from flask import Blueprint, render_template, request
from app.DataAccess.Models import FirstNames, LastNames
import datetime as dt
from app.BusinessLogic.FictionalPerson import FictionalPerson


views_bp = Blueprint(
    'views_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@views_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        error = None
        res = None
        form = request.form
        try:
            amount = int(form['amount'])
            start = dt.datetime.strptime(form['start'], '%Y-%m-%d').date()
            end = dt.datetime.strptime(form['end'], '%Y-%m-%d').date()
            mod11 = True if form.get('mod-11') == 'on' else False
            gender = form['gender-selector']

            res = list()
            count = 0
            while count < amount:
                lastname = LastNames.get_single_lastname().name
                p = FictionalPerson(lastname, start, end)
                if not p.validate_CPR(p.cpr) and mod11:
                    continue
                if gender == 'male':
                    if p.is_male != 'Mand':
                        continue
                    p.first_name = FirstNames.get_single_firstname_by_gender(True).name
                elif gender == 'female':
                    if p.is_male != 'Kvinde':
                        continue
                    p.first_name = FirstNames.get_single_firstname_by_gender(False).name
                else:
                    p.first_name = FirstNames.get_single_firstname().name
                res.append(p)
                count += 1

        except:
            error = 'Invalid input'
        return render_template('index.html', res = res, error = error)
    return render_template('index.html')

@views_bp.route('/metode')
def metode():
    return render_template('metode.html')

@views_bp.route('/api-dokumentation')
def api_dokumentation():
    return render_template('api-dokumentation.html')

