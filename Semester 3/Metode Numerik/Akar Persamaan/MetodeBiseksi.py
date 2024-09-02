def f(x):
    return x**4 - 2*x**2 + x - 2

def bisection(a, b):
    err = 10**(-3)
    if f(a) * f(b) > 0:
        print("Nilai a dan b tidak sesuai")
        return None
    elif f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    xr = (a + b) / 2
    i=0
    while (abs(f(xr)) > err) & (i < 100):
        if f(a) * f(xr) < 0:
            b = xr
        else:
            a = xr
        xr = (a + b) / 2
        i += 1
    print("Iterasi: ", i)
    return xr

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
print("Akar persamaan: ", bisection(a, b))