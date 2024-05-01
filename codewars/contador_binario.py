P = input("Coloque um número para contar os bits: ")

def count_bits(n):
    try:
        N = int(n)
        b = 0
        while N >= 1:
            
            if N%2 == 1:
                b = b + 1

            N = N//2
        
        print("Número de bits com número 1:", b)
        return b 
    
    except:
        print("Invalid Number")

count_bits(P)
