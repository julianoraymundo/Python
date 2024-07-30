list = [0,1,2,3,4,0,5]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)
print(list)