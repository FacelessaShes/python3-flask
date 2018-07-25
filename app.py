# -- coding: UTF-8
from flask import Flask,render_template,request,session
from SQL import select,input,confirm
from pyecharts import Bar
app = Flask(__name__)
app.config['SECRET_KEY']='123455'
REMOTE_HOST = "https://pyecharts.github.io/assets/js"





class User:
    def __inint__(self):
        self.name=''
        self.password=''
    def alter_name(self,i):
        self.name=i
    def alter_password(self,i):
        self.password=i

def loginconfirm():
    i = session.get('usernmae')
    if session.get('state')is None:
        return  u'未登陆'
    elif session.get('state') == 1:
        return u'已登陆'

def bar():
    tile=request.form.get('tile', '')
    x=request.form.get('x','')
    y=request.form.get('y','')
    x=x.split(',')
    y=y.split(',')
    bar = Bar(tile, "")
    bar.add("", x, y)
    return bar
@app.route('/')
def hello_world():
    message = loginconfirm()
    username = u'游客'
    return render_template('index.html',message=message,username=username)


@app.route('/login',methods=['get'])
def login():
    return render_template('login.html')


@app.route('/login',methods=['post'])
def loging():
    a=User()
    a.alter_name(request.form.get('username',''))
    a.alter_password(request.form.get('password',''))
    i=select('username')
    if a.name not in i:
        message= u'未找到用户名 {}'.format(a.name)
        return render_template('index.html', message=message, username=u'游客')
    else:
        j=confirm(a.name)
        if a.password ==j:
            session['username'] = a.name
            session['password'] = a.password
            session['state']=1
            message=u'登陆成功'
            username=a.name
            return render_template('index.html', message=message, username=username)
        else:
            message= u'密码错误'
            return render_template('index.html', message=message, username=u'游客')



@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/bar')
def bar():
    if session.get('state') == 1:
        message = loginconfirm()
        name = session.get('username')
        return render_template('bar.html', message=message, username=name)
    else:
        return render_template('index.html', message=u'请先登录', username=u'游客')



@app.route('/bar',methods=['post'])
def baring():
    tile=request.form.get('tile', '')
    x=request.form.get('x','')
    y=request.form.get('y','')
    x=x.split(',')
    y=y.split(',')
    bar = Bar(tile, "")
    bar.add("", x, y)
    return render_template(
        "pychart.html",
        myechart=bar.render_embed(),
        host=REMOTE_HOST,
        script_list=bar.get_js_dependencies(),
    )


@app.route('/register',methods=['Post'])
def registering():
    a=User()
    a.alter_name(request.form.get('username',''))
    a.alter_password(request.form.get('password',''))
    i=select("username")

    if a.name not in i:
        input(a.name,a.password)
        message = u'注册成功'
        return render_template('index.html', message=message, username=u'游客')
    else:
        message = u'该用户已被注册'
        return render_template('index.html', message=message, username=u'游客')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
