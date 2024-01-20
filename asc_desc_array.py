n=int(input("Enter the number of values:"))
b=[]
for i in range (0,n):
    a=int(input("Enter number:"))
    b.append(a)

print(b)

for i in range(0,n):
    if b[i]<b[i+1]:
        print("True")
    else:
        print("False")
    break