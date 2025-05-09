from flask import Blueprint , render_template , redirect
from flask_login import login_required , current_user
from models.auth import User

users = Blueprint("users" , __name__ , static_folder="../static/" , template_folder="../templates/" , url_prefix="/users/")



@users.route('/<int:user_id>')
@login_required
def index(user_id):
    user = User.query.get(user_id)
    print(user)
    if user:
        return render_template('users/show-user.html' , user=user)
    else:
        return redirect('estates.index')

