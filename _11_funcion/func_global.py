

x = 50

def func():
    global x
    print('x es ', x)
    x = 2
    print('Ahora x es : ', x)

func()
print('x sigue siendo : ', x )