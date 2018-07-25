from pyecharts import Bar
REMOTE_HOST = "https://pyecharts.github.io/assets/js"
script_list=bar.get_js_dependencies()
def bar():
    from pyecharts import Bar
    tile=request.form.get('tile', '')
    x=request.form.get('x','')
    y=request.form.get('y','')
    x=x.split(',')
    y=y.split(',')
    bar = Bar(tile, "")
    bar.add("", x, y)
    return bar