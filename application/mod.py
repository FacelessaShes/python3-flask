import time
from flask import session,render_template



def timing(function):
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print '[Function: {name} finished, spent time: {time:.5f}s]'.format(name = function.__name__,time = t1 - t0)
        return result
    return function_timer



