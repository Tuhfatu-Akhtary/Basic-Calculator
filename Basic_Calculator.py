print("Welcome to the Calculator Project!")
print("Please Select an Operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option=int(input("Select an operation to perform: "))


if option == 1:
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    n3=n1+n2
    print("Addition is : "+ str(n3))

elif option==2:
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    n3=n1-n2
    print("Subtraction is is : "+ str(n3))

elif option==3:
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    n3=n1*n2
    print("Multiplication is : "+ str(n3))

elif option==4:
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    n3=n1/n2
    print("Division is : "+ str(n3))

else:
    print("Invalid Input")