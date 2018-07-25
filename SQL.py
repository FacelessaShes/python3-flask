# -- coding: UTF-8
import MySQLdb
#pip install MySQL_python-1.2.5-cp36-none-win32.whl
db = MySQLdb.connect("localhost", "localhost", "zhao123", "test", charset='utf8' )
cursor = db.cursor()
def select(column):
    a=cursor.execute('select {} from User '.format(column))
    a=list(cursor.fetchall())
    j=[]
    for i in a:
        i=list(i)
        j=j+i
    return j

def input(name,password):
    cursor.execute("INSERT INTO User VALUE('{}','{}')".format(name,password))
    db.commit()

def confirm(name):
    cursor.execute(" select userpassword from User where username='{}'".format(name))
    a=list(cursor.fetchall())
    j=[]
    for i in a:
        i=list(i)
        j=j+i
    return j[0]

