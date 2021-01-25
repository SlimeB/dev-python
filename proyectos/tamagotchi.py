#el proyecto conxiste en crear un tamagotchi que funcione a base de comandos y por turnos
#paso 1: hacer las variables que afectan al tamagotchi
salud = 5
animo = 5
hambre = 5
sueño = 5
higiene = 5
#varieables que no afectan al tamagotchi
estado = True


#paso 2: crear los comandos que afectaran a las variables
def imprimir():
    print("\n" "salud: " + str(salud))
    print("animo: " + str(animo) + "\n")
    print("hambre: " + str(hambre))
    print("sueño: " + str(sueño))
    print("higiene: " + str(higiene) + "\n")

def sumar(var, int):
    if var < 5:
        var += int
    return var
    
    

def restar(var):
    if var > 0:
        var -= 1
        return var
    elif var == 0:
        global salud
        global animo
        salud -= 1
        animo -= 1

    
"""
def comer():
    global hambre
    if hambre < 5:
        hambre += 1
    
    global higiene
    if higiene > 0:
        higiene -= 1
    elif higiene == 0:
        global salud
        global animo
        salud -= 1
        animo -= 1

def dormir():
    global sueño
    global hambre
    output1 = sumar(sueño)
    restar(hambre)
    

def limpiar():
    global higiene
    sumar(higiene)
"""
def salida():
    global estado
    estado = False

"""bucle que mantiene el juego andando"""

while estado == True:
    msg = input()

    if msg == 'comer':
        sumar(hambre, 1)
        restar(higiene)

    if msg == "dormir":
        dormir()

    if msg == "limpiar":
        limpiar()

    if msg == "salir":
        print("adios")
        salida()
    else:
        imprimir()
        
