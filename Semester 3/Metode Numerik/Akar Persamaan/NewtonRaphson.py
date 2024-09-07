def f(x):
    return x**4 - 2*x**2 + 1*x - 2

def df(x):
    return 4*x**3 - 4*x + 1

def newton_raphson(x0):
    x = x0
    while abs(f(x)) > 1e-5:
        x = x - f(x)/df(x)
        print("x="+str(x))
    return x

print("Nilai akar adalah x="+str(newton_raphson(1)))