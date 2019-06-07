mylist=[]
n=int(input("enter the number"))
for i in range(0,n):
    x=int(input("enter the number"))
    mylist.insert(x,i)
print(mylist)
print(min(mylist))
