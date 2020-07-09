from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo, ValidationError


# from app import Users


class GymnastsForm(FlaskForm):
    firstname = StringField(
        'First Name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    lastname = StringField(
        'Last Name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    age = IntegerField(
        'Age',
        validators=[
            DataRequired(),
            NumberRange(min=0, max=110)
        ]
    )

    submit = SubmitField('Add a Gymnast')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired()
                             ]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ]
                                     )

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ]
                        )

    password = PasswordField('Password',
                             validators=[
                                 DataRequired()
                             ]
                             )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    # def validate_email(self, email):
    #     user = Users.query.filter_by(email=email.data).first()
    #
    #     if user:
    #         raise ValidationError('Email already in use')
