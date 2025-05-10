from flask import Blueprint , render_template , redirect , url_for
from flask_login import login_required , current_user
from models.auth import User

users = Blueprint("users" , __name__ , url_prefix="/users/")



@users.route('/<int:user_id>')
@login_required
def index(user_id):
    user = User.query.get(user_id)
    # UNTIL WE ADD MODELS 
    properties  = None 
    clients  = None
    #-----

    if user:
        return render_template('users/show-user.html' , user=user , properties=properties , clients = clients)
    else:
        return redirect('estates.index')
