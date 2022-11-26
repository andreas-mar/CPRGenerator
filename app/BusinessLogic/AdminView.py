from flask_admin.contrib.sqla import ModelView
from app.DataAccess.Models import User
from flask import session, redirect

class AdminView(ModelView):
    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')