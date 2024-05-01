def solution(number):
    soma = 0
    if 0 >= number:
        return 0
    number = number - 1
    while number != 0:
        if number % 3 == 0:
            soma = soma + number
            number = number - 1
        if number % 5 == 0:
            soma = soma + number
            number = number - 1
        else:
            number = number - 1
    print(soma)


s = 14
solution(s)