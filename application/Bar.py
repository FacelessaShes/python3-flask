#coding:utf-8
from flask import Blueprint,request,session,render_template
from pyecharts import Bar
from admin import loginconfirm
from mod import timing

app_bar = Blueprint('Bar', __name__)



@app_bar.route('/bar')
def bars():
    if session.get('state') == 1:
        message = loginconfirm()
        name = session.get('username')
        return render_template('bar.html', message=message, username=name)
    else:
        return render_template('index.html', message=u'请先登录', username=u'请先登陆')


@app_bar.route('/bar',methods=['post'])
@timing
def baring():
    REMOTE_HOST = "https://pyecharts.github.io/assets/js"
    title=request.form.get('tile', '')
    x=request.form.get('x','').split(',')
    y=request.form.get('y','').split(',')
    bar = Bar(title, "")
    bar.add("", x, y)
    return render_template(
        "pychart.html",
        myechart=bar.render_embed(),
        host=REMOTE_HOST,
        script_list=bar.get_js_dependencies(),
    )