n = 1902

def LeapYear(int):
    if n % 4 == 0 and (n % 400 == 0 or n % 100 != 0):
        print(True)
    else:
        print(False)

LeapYear(n)