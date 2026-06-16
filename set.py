

sett1 = {0,0,1,2,3,4,5,6}
sett2 = {4,5,6,7,8,9}


print("set 1 :",sett1)
print("set 2 :",sett2)
print()

#  operation on sets ...
#  use  "  _update " for updating the value of set 1 (set function is operating on) ...

print( "union of sets                 : " , sett1.union(sett2))                 # or use operator  => " | "
print( "intersection of sets          : " , sett1.intersection(sett2))          # or use operator  => " & "
print( "difference in sets            : " , sett1.difference(sett2))            # or use operator  => " - "
print( "symmetric difference of sets  : " , sett1.symmetric_difference(sett2))  
print( "is set 1 disjoint of set 2    : " , sett1.isdisjoint(sett2))
print( "is set 1 a subset of set 2    : " , sett1.issubset(sett2))
print( "is set 1 superset of set 2    : " , sett1.issuperset(sett2))
print()

#  functions can be operated on sets ...

sett1.add(7)              # add the element in the set
print(sett1)  
sett1.remove(7)           # removes the element from set if present else returns false
print(sett1)
sett1.update((7,8))       # add more than one element
print(sett1)
sett1.pop()               # delete the last element according to stored sequence
print(sett1)
sett1.discard(8)          # delete the element 
print(sett1)
sett2 = sett1.copy()      # copies the set operated on 
print(sett2)
sett1.clear()             # clears the set ( delete all the elements )
sett2.clear()
print(sett1)
print(sett2)


sett1 = { 43,67,36,49,4,6,5,55,38,59,327,6 }


#  program to print minimum and maximum element of the set and sum of all elements 

for i in sett1 :                                  # used for alloction of an element from set
    min = i                                       # to min and max variable for comparison of
    max = i                                       # elements present in the set
    break
sum = 0
for j in sett1 :
    sum += j                                      # to sum the elements
    if j<min :                                    # condition to find minimum element
        min = j
    elif j>max :                                  # condition to find maximum element
        max = j

print("maximum element : ",max)
print("minimum element : ",min)
print("sum of elements : ",sum)