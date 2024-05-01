def digital_root(n):
    def calcular(t):
        j = 0
        T = str(t)
        for i in T:
            I = int(i)
            j = j + I
        t = j
        return t
    while True:
        if n >= 10:
            n = calcular(n)
        else:
            break
    

    n = calcular(n)
    print(n)
    return n

    
    

digital_root(493193)