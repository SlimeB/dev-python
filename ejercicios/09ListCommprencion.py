x = 3
y = 3
z = 3
n = 4

"""def cubo(int1, int2, int3):
    n = int1 + int2 + int3
    c = [0, 0, 0]

    while c[0] < int1 and c[1] < int2 and c[2] < int3:
        c[2] += 1

        if c[2] == int3+1:                                    <--- solución de mierda
            c[1] += 1
            c[2] = 0
        elif c[1] > int2-1 and c[2] == int3:
            c[0] += 1
            c[1] = 0
        
        print(c)

cubo(x, y, z)"""
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ]) """<--- mejor solucion"""