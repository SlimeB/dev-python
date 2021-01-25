x = 5
y = 2

def restar():
    global x
    global y
    if x > 0:
        x += y

def test(stat):
    newStat = stat
    if newStat > 0:
        newStat += 1
    return newStat 

def app():
    newValor = test(x)
    global x 
    x = newValor
    print(x)
    

app()