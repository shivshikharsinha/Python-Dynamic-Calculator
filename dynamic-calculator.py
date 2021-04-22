#Greetings
print("Hello!, Select Operation you want to do: ")
#Operation to be performed.
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
#Taking Input for Operation to be performed.
print()

while True:
    i=float(input("Select Choice (1/2/3/4) : "))
    print()
    n=4
    while (i<=n):
        if (i == 0):
            print()

        elif (i==1):
                print("Input Two Numbers to Add : ")
                num1=float(input("Enter Number 1: "))
                num2= float(input("Enter Number 2: "))
                result= num1 + num2
                print("The Sum is: ",result)
                print()
        elif(i==2):
                print("Input Two Numbers to Subtract : ")
                num1 = float(input("Enter Number 1: "))
                num2 = float(input("Enter Number 2: "))

                result = num1 - num2
                print("The Difference is: ", result)
                print()
        elif(i==3):
                print("Input Two Numbers to Multiply : ")
                num1 = float(input("Enter Number 1: "))
                num2 = float(input("Enter Number 2: "))
                result = num1 * num2
                print("The Product is: ", result)
                print()
        elif (i == 4):
                print("Input Two Numbers to Divide : ")
                num1 = float(input("Enter Number 1: "))
                num2 = float(input("Enter Number 2: "))
                result = num1 / num2
                print("The Division is: ", result)
                print()
        break

    else:
       print("Invalid Input !! Please Try Again")
       print()
