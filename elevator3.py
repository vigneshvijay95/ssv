
user_input = int(input(" Enter the floor you want to go :"))
log_list = []
start = 0
end = 5
while(start < end):
    if(start == user_input):
        print(" You are in ", user_input, "floor")
        log_list.append(user_input)
        user_input_two = int(input(" Enter the floor you want to go:"))
        if(user_input_two != user_input):
            user_input = user_input_two
            #print(user_input, lp)

        else:
            print("Entered value is same:")
            continue
        start = 0
    start += 1
print(" Log list:", log_list)
if(user_input >= 5):        
    print(" Incorrect,please try again")