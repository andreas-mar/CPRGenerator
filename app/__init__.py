from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

DEV_MODE = False


db = SQLAlchemy()
admin = Admin(name='Cutcard', template_mode='bootstrap4')

def init_app():
    # Construct application
    app = Flask(__name__)

    # Configure application
    app.secret_key = """[1Nll-VvD}YNh'd}Z),iVE'/`doA(:xYe({4%Ue6A+Xy1rVYmjsxWxi;WEl#_;v"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db?check_same_thread=False'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    #Admin config
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    # Init plugins
    db.init_app(app)
    admin.init_app(app)


    # Get all app features from files
    with app.app_context():
        # Import files shared across app
        from app.API import api
        from app.Service import views

        # Register blueprints
        app.register_blueprint(api.api_bp)
        app.register_blueprint(views.views_bp)


        # Errorhandlers
        #app.register_error_handler(404, administration.page_not_found)

        db.create_all()
        from app.DataAccess.Models import FirstNames, LastNames, User
        from app.BusinessLogic.AdminView import AdminView
        admin.add_view(AdminView(FirstNames, db.session))
        admin.add_view(AdminView(LastNames, db.session))
        admin.add_view(AdminView(User, db.session))


        return app


if __name__ == '__main__':
    app = init_app()
    app.run(debug=False)