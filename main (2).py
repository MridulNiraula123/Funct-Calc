#this program takes start point from user and prints the value 1 by one
def function():
    Num_1 = int(input("Num 1: "))
    Num_2 = int(input("Num 2: "))
    Num_3 = int(input("Enter the difference in the count: "))
    abcd = Num_1
    while (abcd<Num_2):
        print(abcd)
        abcd= abcd+Num_3

eertsfvsd = int(input(" Do you want to know the values between numbers? 1 for Yes and 2 for No: "))
if eertsfvsd == 1:
    function()
    
else:
    print ("You are dumb")