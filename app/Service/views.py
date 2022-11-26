from flask import Blueprint


views_bp = Blueprint(
    'views_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@views_bp.route('/')
def home():
    return 'home'