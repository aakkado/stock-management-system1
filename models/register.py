from flask_wtf import FlaskForm
from wtforms import StringField, EmailField,PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from user import User

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Nome de usuário"})
    
    email = EmailField(validators=[InputRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Email"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Senha"})
    
    submit = SubmitField("Cadastrar")
    
    def validate_email(self, email):
        existing_user_email = User.query.filter_by(
            email=email.data
        ).first()
        
        if existing_user_email:
            raise ValidationError(
                "Email de usuário já cadastrado"
            )