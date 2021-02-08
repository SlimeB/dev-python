def fibo(n = 1):
    if 0 <= n <= 1:
        print(n)
    
    a = 1
    b = 0
    result = 0

    for i in range(n-1):
        result = a + b
        b = a
        a = result
        print(result)

fibo(7)