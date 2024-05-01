s = input()
count = 1
pl = True
r = s[0].upper()
for i in s:
	if pl == True:
		count = count + 1
		pl = False
		continue
	else:
		i = i * count
		r = r + "-" + i.capitalize()
		count = count + 1
