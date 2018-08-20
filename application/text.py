from mod import timing
import time
@timing
def t(i):
    x=0
    for j in range(i):
        x=x+j
    return x

print(t(10))