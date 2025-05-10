from flask import Blueprint , render_template , redirect , url_for , flash , request
from flask_login import login_user, logout_user , current_user
from app.extensions import login_manager , bcrypt , db
from models.auth import User
from forms.auth import LoginForm , SignUpForm

auth = Blueprint("auth" , __name__ , url_prefix="/auth")
login_manager.login_view = 'auth.login'
login_manager.login_message = "Sorry, you need to be logged in to access this route and your account activated"
login_manager.login_message_category = "info"

@login_manager.user_loader
def user_loader(id):
    return User.query.get(id)



@auth.route('/login', methods = ["GET" , "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('estates.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user:
            if user.username == username and bcrypt.check_password_hash(user.password , password) and user.active == 1:
                login_user(user , remember=True)
                if not request.args.get('next') is None:
                    return redirect(request.args.get('next'))
                else:    
                    return redirect(url_for('estates.index'))
            else:
                flash("Your account is correct but wait until admin activate you then you can login" , category="info")

        else:
            flash("Check your account information username or password could be wrong" , category="danger")



    return render_template('auth/login.html' , form=form)


@auth.route('/sign-up',  methods = ["GET" , "POST"])
def signUp():
    if current_user.is_authenticated and current_user.active == 1 :
        return redirect(url_for('estates.index'))

    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        phone_number = form.phone_number.data
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username = username , password = password_hash , email = email , phone_number=phone_number)

        db.session.add(new_user)
        db.session.commit()



        flash("Account created successfully but your account need to activated by admin wait until it activated" , category="info")




    return render_template('auth/signUp.html' , form=form)


@auth.get('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('auth.login'))





