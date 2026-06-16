

dict = { 1:"a",2:"b",3:"c",4:"d",5:"e" }

print( dict.keys())                            # returns all the keys
print( dict.values())                          # returns all the values
print( dict.items())                           # returns all the items

dict.popitem()                                 # deletes the last item
print( dict )
dict.update({5:"e",6:"f"})                     # appends the items
print(dict)

dict.pop(6)                                    # deletes the item based on key
print(dict)

print(dict.get(1))                             # returns the value of the key given

dict1 = dict.copy()                            # copys the dictionary

print(dict1)

del(dict1)                                     # deletes the dictionary



print()
# program to make a dictionary and multiply the values and print it ...

dict1 = {}
multi = 1
for i in range(1,15) :
    dict1[i] = i**2
    multi *= dict1[i]
print(dict1)
print("mutiplication of values = ",multi)



print()
# program to check if the dictionary is empty or not ... 

dict2 = {1:"a"}
if len(dict2) == False :
    print("dictionary is empty")
else :
    print( " dictionary has a value in it ") 