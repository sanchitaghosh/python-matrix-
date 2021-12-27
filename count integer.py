n=int(input("Enter  number: "))
l=[]

for i in range(0,9):
    l.append(i)
    print(l)
while(n!=0):
    a=n%10
    l[a]=l[a]+1       
    n=n//10
    
print(l)
for j in range(len(l)):
    if l[j]>0:
        print(j,end="")
            
