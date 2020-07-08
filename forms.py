from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


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
