from wtforms import IntegerField, SelectField, SubmitField, StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class DwfForm(FlaskForm):
    sore = IntegerField('Sore', validators=[DataRequired()])
    category = SelectField('Category', choices=[('5', '理科'), ('1', '文科')], validators=[DataRequired()])
    submit = SubmitField('查询')
