from flask import Blueprint
from flask_login import login_required , current_user

estates = Blueprint("estates" , __name__ )



@estates.route('/')
@login_required
def index():
    return f"Hello {current_user.username}"


