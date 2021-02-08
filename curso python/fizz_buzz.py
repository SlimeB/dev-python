def fizz_buzz(n: int = 1) -> None:
    """
    dependiendo de si es o no un multiplo de 3, 5 o ambos imprime "fizz", "buzz" o "fizz buzz" respectivame.
    :param n: numero mas grande en la lista.
    :return: un str ya sea el numero de turno, fizz, buzz o fizz buzz.
    """
    if n % 3 == 0 and n % 5 == 0:
        print("fizz buzz")  
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
fizz_buzz()

i = 0