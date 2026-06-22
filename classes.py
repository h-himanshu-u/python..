
class factorial :

    def __init__(self) :
        print()
        print(" hello welcome to the math lab !!! ")
    def __del1__(self) :
        print()
        print(" thank you for visiting the math lab !!! ")

    def factorial(self,n) :
        self.n = n 
        if self.n < 0 :
            return "factorial not possible !!! "
        elif self.n == 0 :
            return 1
        else :
            fact = self.n * self.factorial(self.n - 1)
    
            return   fact
        
class maximum :
    def maximum(self,a,b,c) :
        self.a = a
        self.b = b
        self.c = c
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

class math(factorial) :
    def start(self,n) :
        if n == 1 :
            a = int(input(" enter the number for factorial : "))
            object_1 = factorial()
            print("factorial of the number ",a," is : ",object_1.factorial(a))
            object_1.__del1__()
        elif n == 2 :
            a= int(input(" enter the first number : "))
            b= int(input(" enter the second number : "))
            c= int(input(" enter the third number : "))
            object_2 = maximum()
            print("maximum among three numbers ( ",a," , ",b," , ",c," ) is : " , object_2.maximum(a,b,c))

print("what you want to do ")
print("1. factorial of a number ")
print("2. maximum among three numbers ")
n = int(input("enter your choice : "))
object_3 = math()
object_3.start(n)