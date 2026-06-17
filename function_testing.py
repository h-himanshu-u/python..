
# types of arguments and parameter combinations in the functions ...

def add(a,b):        
    return a+b
print( add(5,6))                                    # default arfuments

c = 7
d = 4
print( add(d,c))                                    # positional arguments


def subtraction(a,b=10) :                           
    return b-a 
print( subtraction(5) )
print( subtraction( a= 55, b = 43 ) )               # keyword arguments

def add_listtt(*a) :                                # variable length arguments
    return sum(a)
print(add_listtt(1,2,3,4,5,6,7,8,9,0))

# function for printing maximum element among three elements ...
def maximum(a,b,c) :
    if a > b :
        if a > c : 
            return a
        else :
            return c 
    else :
        if b>c :
            return b 
        else :
            return c


# function to return sum of elements of a list ...
def sum_list(a) :
    
    return sum(a)


# a lambda function for  square root of an element ...
x = lambda a:a**(1/2)


a = int(input("enter the number : "))
print("square root of ",a," is : ",x(a))
print("maximum among three numbers ( 34 , 56 , 67 ) is : " , maximum(34,56,67))
print("sum of all the elements of the list is : " , sum_list([0,2,54,23,6,8,45,6,34,56]))
