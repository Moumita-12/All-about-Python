friends = ["a", "b", "c","d"]
#print single index
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-2])

#replace with other value
friends[0] = "x"
print(friends)

#print in range
print(friends[0:3]) #returns a new list

#print values
for name in friends:
    print(name)

#insert in last
friends.append("arohi")
print(friends)

#insert with specific index
friends.insert(0, "nila")
print(friends)

#print using length
i=0
while i<len(friends):
    print(friends[i])
    i=i+1

#clear the list
friends.clear()
print(friends)
