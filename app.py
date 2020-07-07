from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ


app = Flask(__name__)

# make more secure <---------------------------------------
app.config['SECRET KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \ environ.get('MYSQL_USER') + \
                                                       ':' + \ environ.get('MYSQL_PASSWORD') + \
                                                       '@' + \ environ.get('MYSQL_HOST') + \
                                                       ':' + \ environ.get('MYSQL_PORT') + \
                                                       '/' + \ environ.get('MYSQL_DB_NAME')


db = SQLAlchemy(app)


class Gymnasts(db.Model):
    gymnast_id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'Name: ' + self.firstname, + ' ' + self.lastname + '\n'
                                                                   'Gymnast ID: ' + self.gymnast_id
            ]
        )


@app.route('/')
@app.route('/home')
def home():
    gymnast_data = Gymnasts.query.all()
    return render_template('home.html', title='Homepage', gymnasts=gymnast_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/create')
def create():
    db.create_all()
    gymnast = Gymnasts(firstname='Paul', lastname='Lagah')
    db.session.add(gymnast)
    db.session.commit()
    return "Added the table and populated it with a Record"


@app.route('/delete')
def delete():
    db.drop_all()
    db.session.query(Gymnasts).delete()
    db.session.commit()
    return "Bye Bye Gymnast"


if __name__ == '__main__':
    app.run()
