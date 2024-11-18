# app/__init__.py

# Flaskというウェブアプリケーションを作るためのライブラリをインポートします。
from flask import Flask
# データベースのマイグレーションを管理するためのライブラリをインポートします。
from flask_migrate import Migrate
# ユーザーのログイン管理をするためのライブラリをインポートします。
from flask_login import LoginManager
import os  # OSに関する機能を使うためのライブラリ
from .extensions import db  # データベースの設定を別のファイルからインポートします。

# マイグレーションとログイン管理のためのインスタンスを作ります。
migrate = Migrate()
login_manager = LoginManager()

# アプリケーションを作るための関数です。
def create_app():
    app = Flask(__name__)  # Flaskアプリケーションを作ります。
    # データベースの設定をします。
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True  # デバッグモードを有効にします。
    app.config['SECRET_KEY'] = os.urandom(24)  # セキュリティのための秘密の鍵を作ります。

    # データベース、マイグレーション、ログイン管理をアプリに登録します。
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # ルート（URLの処理）を別のファイルからインポートしてアプリに登録します。
    from .routes import bp
    app.register_blueprint(bp)

    return app  # 作ったアプリケーションを返します。

# ユーザーのIDを使って、データベースからユーザーを取得する関数です。
@login_manager.user_loader
def load_user(user_id):
    from .models import User  # ユーザーモデルをインポートします。
    return User.query.get(int(user_id))  # ユーザーIDに基づいてユーザーを取得します。