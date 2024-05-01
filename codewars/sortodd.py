def sort_array(source_array):
    odd = list()
    position = list()
    count = 0
    for i in source_array:
        if i % 2 > 0:
            odd.append(i)
            position.append(count)
        count += 1
    odd.sort()
    count = 0
    for i in position:
        source_array[i] = odd[count]
        count += 1
    return source_array