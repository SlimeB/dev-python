import random
maxNum = 3
num = random.randint(0,maxNum)
intentos = 3

while intentos != 0:
    respuesta = input("crees que el numero es: ")

    if respuesta == str(num):
        print("¡¡correcto!!")
        intentos = 0
    else:
        print("respuesta incorrecta")
        intentos -= 1

        if respuesta > str(maxNum) :
            print("te pasaste")
        
        if respuesta < str(maxNum):
            print("te falto")
