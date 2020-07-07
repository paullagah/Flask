from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

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

    submit = SubmitField('Add a Gymnast')