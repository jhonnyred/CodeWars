def expanded_form(num):
    stri = str(num)
    result = ''
    count = len(stri)
    for i in stri:
        if int(i) != 0:
            result += i
            for x in range(count - 1):
                result += '0'
            result += ' + '
        count = count - 1
    result = result[:len(result) - 3] 
    return result