# app/forms.py

# Flask-WTFをインポートします。
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# ユーザー登録用のフォームを作ります。
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  # ユーザー名のフィールド
    email = StringField('Email', validators=[DataRequired(), Email()])  # メールアドレスのフィールド
    password = PasswordField('Password', validators=[DataRequired()])  # パスワードのフィールド
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  # 確認用パスワードのフィールド
    submit = SubmitField('Sign Up')  # 登録ボタン

# ログイン用のフォームを作ります。
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # メールアドレスのフィールド
    password = PasswordField('Password', validators=[DataRequired()])  # パスワードのフィールド
    submit = SubmitField('Login')  # ログインボタン