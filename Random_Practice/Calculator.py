num1 = float(input("Insert the first number :  "))
num2 = float(input("Insert the second number : "))
operate= float(input("Enter the operation : \n1 for Addition \n2 for Substraction \n3 for Multiplication \n4 for Division \n5 for Exit \n"))
if operate == 1 :
    print(num1 + num2)
elif operate == 2 :
    print(num1-num2)
elif operate == 3:
    print(num1*num2)
elif operate == 4:
    print(num1/num2)
else:
    print("Wrong Input")
