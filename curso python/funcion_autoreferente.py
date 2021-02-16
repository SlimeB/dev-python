def fact(n):
    if n <= 1:
        return 1
    else:
        return n * int(fact(n-1))

print(fact(0))

"""
fijarse que en la función se está sitando la misma función
esto se puede hacer puesto que se está sitando hasta que n
es 1, por ponerlo en otra forma es como resolver x, de
a(b(c(x)))
"""
