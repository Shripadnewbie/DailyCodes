li = [2, False, 'y', -9, 'string', 8, 5, -10, 2, 'y', 10, 'z', -8, -8, -3, -8, 'a', -10, '0', 'b', -2, 9, 0, 0, 0, 0]
fli = []
for num in li:
    if (num == 0 or str(num) == '0') and type(num) != bool:
        fli.insert(-1,0)
for inum in li:   if type(inum)!=bool:
        while 0 in li and type(inum)==int or str :
           li.remove(inum)
        while '0' in li and type(inum)==str:
           li.remove(inum)
li.extend(fli)
print(fli)
print(li)


