
x=int(input("enter first number:"))
y=int(input("enter first number:"))
z=int(input("enter first number:"))

if(x>y)and(x>z):

    print("small number",x)
elif(y>x)and(y>z):

    print("number is medium",y)
else:
    print("greater number is",z)