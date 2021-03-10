log_list=[]
floor=0
def get_input():
    floor_input = int(input("Please select floor 1-4:  "))
    return floor_input


def move_up():
    global floor_inputs
    global current_floor
    global log_list
    while floor_input >= current_floor:
        print ("You are currently on floor:  " + str(current_floor))
        log_list.append(current_floor)

        if floor_input == current_floor:
            print ("You have arrived at floor " + str(current_floor))
            floor_input = get_input()
            print(log_list)
        current_floor += 1
    return move_up  
def move_down():
    global floor_input
    global current_floor
    global log_list
    while floor_input < current_floor:
        current_floor -= 1
        print ("You are currently on floor:  " + str(current_floor))
        
        if floor_input == current_floor:
            print ("You have arrived at floor " + str(current_floor))
        if floor_input >= 5:
            print ("floor is not available")
        print(log_list)
    return move_down()
if __name__ == "__main__":
    current_floor = 1
    floor_input = get_input()
    if (floor_input >= 5 ) :
        print("floor is not available")
    else:
        if floor_input >= current_floor :
            move_up()
        else:
            move_down()