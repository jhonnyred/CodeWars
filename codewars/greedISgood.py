def score(dice):
    
    def cem(a):
        return a*100
    
    count = dict()
    points = int()
    
    for i in dice:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for k,v in count.items():
        
        if str(k) == '1':
            if v >= 3:
                points += 1000
                points += (v%3) * cem(1)
            elif v < 3:
                points += (v%3) * cem(1)
        
        elif str(k) == '2':
            if v >= 3:
                points += cem(2)
        
        elif str(k) == '3':
            if v >= 3:
                points += cem(3)
        
        elif str(k) == '4':
            if v >= 3:
                points += cem(4)
        
        elif str(k) == '5':
            if v >= 3:
                points += cem(5)
                points += (v%3) * 50
            elif v < 3:
                points += (v%3) * 50
        
        elif str(k) == '6':
            if v >= 3:
                points += cem(6)
    
    print(points, count)
    return points