# app/models.py

# データベースの設定をインポートします。
from .extensions import db  # extensions.pyからdbをインポートします。
from flask_login import UserMixin  # UserMixinをインポート

# ユーザーの情報を管理するためのモデル（設計図）を作ります。
class User(db.Model, UserMixin):  # UserMixinを継承
    """ユーザーのモデル"""
    id = db.Column(db.Integer, primary_key=True)  # ユーザーのID（番号）を定義します。
    username = db.Column(db.String(20), unique=True, nullable=False)  # ユーザー名を定義します。
    email = db.Column(db.String(120), unique=True, nullable=False)  # メールアドレスを定義します。
    password = db.Column(db.String(60), nullable=False)  # パスワードを定義します。

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"  # ユーザーの情報を表示するための方法です。