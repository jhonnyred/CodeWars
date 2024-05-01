def zeros(n):
    first = True
    result = 1
    count = 0
    for i in range(n):
        if first == True:
            first = False
            continue
        else:
            result += result*i
    
    result2 = str(result)
    for i in result2[::-1]:
        if i == '0':
            count += 1
        else:
            break
    return count