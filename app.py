# -- coding: UTF-8
from flask import Flask,render_template
from application.Bar import app_bar
from application.admin import admin_bp,loginconfirm


app = Flask(__name__)
app.config['SECRET_KEY']='123455'
app.register_blueprint(app_bar, url_prefix='')
app.register_blueprint(admin_bp, url_prefix='')

@app.route('/')
def index():
    message = loginconfirm()
    username = u'游客'
    return render_template('index.html',message=message,username=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
