
fp= open("test_file.python11","r")
print(fp)
if(fp):
    print("File opened successfully")   
else:
    print("File not opened successfully")  
print()
content = fp.read()
print("content of the file is : \n",content)
fp.close()


fp= open("test_file.python11","a")

list_1 = []
n = int(input("enter the number of lines to be written in the file : "))
for i in range(1,n+1) : 
    a = input("enter the line to be written in the file :  ")
    list_1.append(a)
if n != True:
    print("no lines to be written in the file !!! ")
else :
    print("\n lines written successfully in the file !!! ")
fp.writelines(list_1)
fp.close()




