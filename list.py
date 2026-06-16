# basic list functions ..
# for tuple used as  as for list 
# permitted tuple functions => index , len , count ...
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = []

print(len(l1))                   # returns the length of list
print(l1 + l2)
print(l1.index(5))               # returns the index value of the element given as parameter
l3 = l1.copy()                   # returns the copy of that list
print(l3)
l3.clear()
print(l2.count(8))               # counts the number of times an element appears in list
l1.extend(l2)                    # add multiple elements in the list
print(l1)
l1.append(11)                    # adds an element at the end of list 
print(l1)
l1.pop()                         # removes the last element of list
print(l1)
l1.insert(0,0)                   # inserts the element at the index position given first as parameter
print(l1)


l1.clear()
l2.clear()                       # deletes all the elements
l3.clear()
print()


#       program for finding common elements ...

t1 = [1,2,3,4,5] 
t2 = [2,1,5,6,7,8,5,2,3,5]
t3 = []

for i in t1 :                                      # accessing elements of list t1            
    for j in t2 :                                  # accessing elements of list t2
        if (i == j) and (i not in t3) :            # checking weather the both the elements are equal and is in the t3 list or not
            t3.append(i)                           # add the element in list t3



print("common elements are : ",end = " ")
for i in t3 :                                      # printing elements of list t3
    print(i,end = "  ")

print()



#             program to eleminate duplicate entries for a list ...
print("\n")
t1 = [1,2,2,3,4,5,5,3,6,7,8,8,0,5]
t2 = []
for i in t1 :                                      # accessing elements of the list
    if i not in t2 :                               # checking if the elemets is in list t2
        t2.append(i)                               # adding element in list t2
    else :
        pass

print("unique list :")
print(t2)
print()


 #      program to swap two elements of a list  ... 

list1 = [3,64,42,586,356,57,378,48,64,56,5,55]
print(list1)

a = int(input("enter the element which wants to swap              : "))
b = int(input("enter the element you want to switch element with  : "))

c = list1.index(b)                                                         # storing the index of second element
list1[list1.index(a)] = b                                                  # swaping the values
list1[c] = a                                                               # swaping the values

print(list1)
