# app/routes.py

# Flaskの機能をインポートします。
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm  # フォームをインポートします。
from .models import User  # ユーザーモデルをインポートします。
from .extensions import db  # データベースをインポートします。
from werkzeug.security import generate_password_hash, check_password_hash  # パスワードのハッシュ化を行うためのライブラリをインポートします。

# ルートを管理するためのブループリントを作ります。
bp = Blueprint('main', __name__)

# トップページのルートを定義します。
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')  # トップページのHTMLを表示します。

# ユーザー登録のルートを定義します。
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # 登録フォームを作ります。
    if form.validate_on_submit():  # フォームが送信されたら
        # ユーザーを作成します。
        user = User(username=form.username.data, email=form.email.data)
        user.password = generate_password_hash(form.password.data)  # パスワードをハッシュ化します。
        db.session.add(user)  # データベースにユーザーを追加します。
        db.session.commit()  # 変更を保存します。
        flash('登録が完了しました！', 'success')  # 成功メッセージを表示します。
        return redirect(url_for('main.index'))  # トップページにリダイレクトします。
    return render_template('register.html', form=form)  # フォームを表示します。

# ログインのルートを定義します。
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # ログインフォームを作成
    if form.validate_on_submit():  # フォームが送信されたら
        print("フォームが送信されました")  # デバッグ用メッセージ
        user = User.query.filter_by(email=form.email.data).first()  # メールアドレスでユーザーを検索
        if user:
            print(f"ユーザーが見つかりました: {user.username}")  # ユーザーが見つかった場合のメッセージ
            if check_password_hash(user.password, form.password.data):  # パスワードを確認
                print("ログイン成功")  # デバッグ用メッセージ
                login_user(user)  # ユーザーをログインさせる
                flash('ログインしました！', 'success')  # 成功メッセージを表示
                return redirect(url_for('main.index'))  # トップページにリダイレクト
            else:
                print("パスワードが間違っています")  # パスワードが間違っている場合のメッセージ
                flash('ログインに失敗しました。メールアドレスまたはパスワードが間違っています。', 'danger')  # エラーメッセージを表示
        else:
            print("ユーザーが見つかりませんでした")  # ユーザーが見つからない場合のメッセージ
            flash('ログインに失敗しました。メールアドレスまたはパスワードが間違っています。', 'danger')  # エラーメッセージを表示
    return render_template('login.html', form=form)  # フォームを表示

# ログアウトのルートを定義します。
@bp.route('/logout')
@login_required  # ログインしているユーザーだけがアクセスできるようにします。
def logout():
    logout_user()  # ユーザーをログアウトさせます。
    flash('ログアウトしました。', 'success')  # 成功メッセージを表示します。
    return redirect(url_for('main.index'))  # トップページにリダイレクトします。