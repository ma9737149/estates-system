from models.auth import User
from flask import Blueprint , render_template , flash , redirect , url_for
from flask_login import login_required , current_user
from app import db

admin = Blueprint("admin" , __name__ , url_prefix='/admin/')



@admin.route('/')
@login_required
def index():
    if not current_user.role == 'admin':
        flash('You don\'t have permission to access the admin panel.' , 'danger')
        return redirect(url_for('estates.index'))
    else:
        users = User.query.all()
        # active_users = User.query.filter_by(active=1)
        return render_template('admin.html' , users=users , users_len = len(users))

@admin.route('/activate/<int:user_id>')
@login_required
def activate(user_id):
    if current_user.role == "admin":
        user = User.query.get(user_id)
        if user:
            if user.active == 0:
                user.active = 1
                db.session.commit()
                flash("User is activated succesfully")
                return redirect(url_for('admin.index'))
            else:
                flash("User is already active" , category='info')
                return redirect(url_for('admin.index'))
        else:
            flash('User does not exists' , category='danger')
            return redirect(url_for('admin.index'))

    else:
        flash('You don\'t have permission to access the admin panel.' , 'danger')
        return redirect(url_for('estates.index'))


@admin.route('/deactivate/<int:user_id>')
@login_required
def deactivate(user_id):
    if current_user.role == "admin":
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            flash("User is deactivated successfully")
            return redirect(url_for('admin.index'))
        else:
            flash('User does not exists' , category='danger')
            return redirect(url_for('admin.index'))

    else:
        flash('You don\'t have permission to access the admin panel.' , 'danger')
        return redirect(url_for('estates.index'))

