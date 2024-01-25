from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, RadioField, validators,ValidationError
from wtforms.validators import DataRequired, Email, InputRequired, Length, equal_to
from src.models import User

class AddCarForm(FlaskForm):
    car_manufacturer = StringField('მანქანის მწარმოებელი', validators=[DataRequired()])
    car_model = StringField('მანქანის მოდელი', validators=[DataRequired()])
    car_price = IntegerField('მანქანის ფასი', validators=[DataRequired()])
    image_link = StringField('სურათის ლინკი', validators=[DataRequired()])

    submit = SubmitField('დამატება')


class RegisterForm(FlaskForm):
    username = StringField('შეიყვანეთ იუზერნეიმი', validators=[DataRequired()])
    password = PasswordField('შეიყვანეთ პაროლი',
                             validators=[DataRequired(), Length(min=8, max=64)])
    confirm_password = PasswordField('გაიმეორეთ პაროლი', validators=[DataRequired(),
                                                                     equal_to('password', message='პაროლები არ ემთხვევა')])

    submit = SubmitField('რეგისტრაცია')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("მომხმარებელი გამოყენებულია, გთხოვთ სცადოთ სხვა")

class LoginForm(FlaskForm):
    username = StringField('შეიყვანეთ იუზერნეიმი')
    password = PasswordField('შეიყვანეთ პაროლი')

    submit = SubmitField('შესვლა')
