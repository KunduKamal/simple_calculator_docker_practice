
calculator = 0
message = "select your choice from below:\n \
        to add press : 1 \n \
        to subtract press: 2 \n \
        to multiple press: 3 \n \
        to division press: 4 \n \
        to exit the program: q \n \
        "
while(True):

    print (message)
    # get user input for option 
    mode_select = input("Enter Option:") 
        # check user option 
    if mode_select == "1":
        t_1snumber = int(input("Enter the first number:"))
        t_2ndnumber = int(input("Enter the second number:"))
        calculator = t_1snumber + t_2ndnumber 
        print(calculator)
    elif mode_select == "2":
        t_1snumber = int(input("Enter the first number:"))
        t_2ndnumber = int(input("Enter the second number:"))
        subtract_result = t_1snumber - t_2ndnumber 
        calculator = subtract_result
        print(calculator)
    elif mode_select == "3":
        t_1snumber = int(input("Enter the first number:"))
        t_2ndnumber = int(input("Enter the second number:"))
        multiple_result = t_1snumber * t_2ndnumber 
        calculator = multiple_result
        print(calculator)
    elif mode_select == "4":
        t_1snumber = int(input("Enter the first number:"))
        t_2ndnumber = int(input("Enter the second number:"))
        division_result = t_1snumber / t_2ndnumber 
        calculator = division_result
        print(calculator)
    elif mode_select=="q":
        print("Bye.")
        break
    else:
        print("Calculator can't work")

print("end of code")

