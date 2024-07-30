# o primeiro método usa a função reverse() que modifica o conteudo da variavel e da lista
list1=[4,7,9,2]
list1.reverse()
print(list1)

# slicing
list1=[4,7,9,2]
list2=list1[::-1] # [start:stop:step]
print(list2)

# reversed method
list3=list(reversed(list1))
print(list3)

# reverse whith a for loop 
list2=[]
list1=[4,7,9,2]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)