from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    InputRequired,
    Length,
)


class SendForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), InputRequired(),
                                                 Length(min=3, max=150,
                                                        message='Address must be between 3 and 150 characters.')])
    city = StringField('City', validators=[DataRequired(), InputRequired(),
                                           Length(min=3, max=50, message='City must be between 3 and 50 characters.')])
    submit = SubmitField('Send')
