def sum_eo(n, t):
    eo = 0
    result = 0

    if t in "eo":
        if t == "e":
            eo = 0
        else:
            eo = 1
        
        for i in range(eo, n, 2):
            result += i
            print(result)
    else:
        print(-1)

sum_eo(10, "e")

"""se puede simplificar usando el metodo sum(), en vez de un for
y directamente usando el if para saber si es cualquier cosa, una e o una o"""