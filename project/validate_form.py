from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,validators
from wtforms.validators import DataRequired, Email, Length, ValidationError, NumberRange


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    surname = StringField('Surname', validators=[Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    email = StringField('E-Mail', validators=[Email(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    phone = StringField('Phone', validators=[Length(min=6, max=20, message='Phone number should be between 6-20 characters')])

    def validate_phone(form, field):
        print(field)
        if (len(field.data))>6:
            try:
                int(field.data)
            except Exception as e:
                raise ValidationError('Invalid phone number - Accepts only numbers')

