respuesta = input()

while respuesta != "0":
    print("chose an option:\n1-coock\n2-swim\n3-walk\n4-play videogames\n0-exit")
    respuesta = input()
    print("")

    if respuesta not in "1234":
        print("your choises are in the list up wards, please try awayn")