# run.py

# アプリケーションを作成するための関数をインポートします。
from app import create_app

# アプリケーションを作成します。
app = create_app()

# アプリケーションを実行します。
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードを有効にする