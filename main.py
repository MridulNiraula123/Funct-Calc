#this program is a calculator

#menu for calculator
print("Press 1 for Add")
print("Press 2 for Subtract")
print("Press 3 for Multiply")
print("Press 4 for Divide")

#user choice
choice=int(input("Enter Your Number: "))
#this is for add
if(choice == 1):
    first_number= int(input("first number to add:"))
    second_number = int(input("second number to add:"))
    sum = first_number + second_number
    print(sum)

#this is for subtract
elif(choice == 2):
    first_number=int(input("first number to subtract:"))
    second_number=int(input("second number to subtract:"))
    diffrence = first_number - second_number
    print(diffrence)

#this is for multiply
elif(choice == 3):
    first_number=int(input("first number to multiply:"))
    second_number=int(input("second number to multiply:"))
    product = first_number * second_number
    print(product)

#this is for divide
elif(choice == 4):
    first_number=int(input("first number to divide:"))
    second_number=int(input("second number to divide:"))
    quotient= first_number / second_number
    print(quotient)
    
else:
    print("Invalid Choice")