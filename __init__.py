from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'

    from url_shortner.url_short import url_short
    app.register_blueprint(url_short.bp)

    return app