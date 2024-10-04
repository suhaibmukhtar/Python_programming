#python set operations
#union
a={1,2,3,4}
b={2,3,4,5}
print(a.union(b))
print(a|b)

#intersection
print(a.intersection(b))
print(a&b)

#set difference
print(a-b)
print(b-a)
#symmetric difference
print((a-b).union(b-a))
