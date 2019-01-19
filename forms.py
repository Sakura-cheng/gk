from wtforms import IntegerField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class DwfForm(FlaskForm):
    sore = IntegerField('Sore', validators=[DataRequired])
    category = SelectField('Category', choices=[('0', '理科'), ('1', '文科')], validators=[DataRequired])
    submit = SubmitField('Check')
