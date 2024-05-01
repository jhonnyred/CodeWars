s = input()
spaces = []
cont = 0
l = None
#primeiro 'for' para identificar onde estão os espaços
for i in s:
    if i == " ":
        spaces.append(cont)
    cont = cont + 1

#segundo 'for' para adicionar as palavras na lista atrávés dos espaços, foi necessário criar
# variável para identificar a primeira palavra, por conta dos espaços presentes nas palavras 
primeira = True
palavras = []
antecessor = 0
if len(spaces) == 0:
    palavras.append(s)
else:
    for i in spaces:
        if primeira == True:
            palavras.append(s[antecessor:i])
            primeira = False
            antecessor = i
        else:
            palavras.append(s[antecessor + 1:i])
            antecessor = i
    palavras.append(s[antecessor + 1:])

#Último 'for' para identificar quais as menores palavras dentro da lista de palavras
l = len(palavras[0])
for i in palavras:
    if l > len(i):
        l = len(i)

print(spaces)
print(palavras)
print(l)