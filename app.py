from flask import Flask, url_for, redirect, request
from flask import render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_login import LoginManager
from forms import GymnastsForm, RegistrationForm, LoginForm, ViewForm  # , #UpdateGymnastForm
from flask_login import login_user, current_user, logout_user, login_required, UserMixin

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = '919c92fab903330df5b2f66c22d3b22b'  # environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class Gymnasts(db.Model):
    gymnast_id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Name: ' + self.firstname, + ' ' + self.lastname + '\n'
                                                                   'Gymnast ID: ' + self.gymnast_id
            ]
        )


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(
            ['UserID: ', str(self.id), '\r\n', 'Email: ', self.email, 'Name: ', self.firstname, ' ', self.lastname])


@app.route('/')
@app.route('/home')
def home():
    gymnast_data = Gymnasts.query.all()
    return render_template('home.html', title='Homepage', gymnasts=gymnast_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = GymnastsForm()
    if form.validate_on_submit():
        gymnast_data = Gymnasts(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            age=form.age.data
        )
        db.session.add(gymnast_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('gymnast.html', title='Add a gymnast', form=form)


# @app.route('/gymnast_delete', methods=['GET', 'POST'])
# @login_required
# def gymnast_delete():
#     id = Gymnasts.gymnast_id
#     firstname = Gymnasts.firstname
#     lastname = Gymnasts.lastname
#     age = Gymnasts.age
#     db.session.delete(id, firstname, lastname, age)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
            email=form.email.data,
            password=hash_pw,
            firstname=form.firstname.data,
            lastname=form.lastname.data
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/view/', methods=['GET', 'POST'])
def view():
    form = ViewForm()
    gymnast_all = Gymnasts.query.all()
    if form.validate_on_submit():
        gymnast_data = Gymnasts.query.filter_by(gymnast_id=form.gymnast_id.data).all()
        return render_template('view.html', title='View Gymnasts', form=form, gymnasts=gymnast_data)
    return render_template('view.html', title='View Gymnasts', form=form, gymnasts=gymnast_all)


# @app.route("/account", methods=['GET', 'POST'])
# @login_required
# def update():
#     form = UpdateGymnastForm()
#     if form.validate_on_submit():
#          = form.firstname.data
#          = form.lastname.data
#          = form.age.data
#     elif request.method == 'GET':
#
#     return render_template('update.html', title='Update Gymnast', form=form)

@app.route('/create')
def create():
    db.create_all()
    gymnast = Gymnasts(firstname='Paul', lastname='Lagah', age=28)
    db.session.add(gymnast)
    db.session.commit()
    return "Added the table and populated it with a Record" and redirect(url_for('home'))


@app.route('/delete')
def delete():
    db.drop_all()
    db.session.query(Gymnasts).delete()
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
