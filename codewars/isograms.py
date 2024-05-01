def is_isogram(string):
    isogram = True
    string = string.upper()
    lista = []
    for i in string:
        lista.append(i)
    lista2 = []
    for i in lista:
        lista2.append(lista.count(i))
    for i in lista2:
        if i >= 2:
            isogram = False
            break


    
    print(lista2)
    print(lista)
    print(isogram)
    return isogram

tring = input("Qual palavra vc quer saber se é um isograma? ")
is_isogram(tring)