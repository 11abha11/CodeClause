# Simple Calculator in Python

print("\n\n\n\n\n****************************SIMPLE CALCULATOR IN PYTHON****************************\n\n")
ch = int(input("Enter the number of times you want to perform the operation : "))
while(ch>0):
    num1 = int(input("\n\nEnter your first number :  "))
    num2 = int(input("Enter your second number :  "))

    print("\nSelect the operation to be performed")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

    op = int(input("\nEnter your choice : "))

    if (op==1):
        print ("\nThe sum of", num1, "and", num2,"is: ", num1+num2)

    elif(op==2):
        print ("\nThe difference between", num1, "and", num2,"is: ", num2-num1)

    elif(op==3):
        print ("\nThe product of", num1, "and", num2,"is: ", num1*num2)

    elif(op==4):
        if(num2==0):
            print ("Error! Cannot divide by zero.")
        else:
            print ("\nThe quotient of", num1, "by", num2,"is: ", num1/num2)

    elif(op==5):
        print ("\nThe modulus of", num1, "by", num2,"is: ", num1%num2)

    else:
        print ("Invalid input")

    print("\n\n-----------------------------------------------------------------------------------\n\n")
    ch-=1