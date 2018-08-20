#coding:utf-8
from flask import Blueprint,request,session,render_template
from model.SQL import select,input,confirm
admin_bp = Blueprint('admin', __name__)
from mod import timing
class User:
    def __inint__(self):
        self.name=''
        self.password=''
    def alter_name(self,i):
        self.name=i
    def alter_password(self,i):
        self.password=i


def loginconfirm():
    if session.get('state')is None:
        return  u'未登陆，点我登陆'
    elif session.get('state') == 1:
        return u'已登陆'

@admin_bp.route('/login',methods=['get'])
def login():
    return render_template('login.html')


@admin_bp.route('/login',methods=['post'])
@timing
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


@admin_bp.route('/register')
def register():
    return render_template('register.html')


@admin_bp.route('/register',methods=['Post'])
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