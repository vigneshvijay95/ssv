log_list=[]
floor = int(input("ENter Your Answer"))
def get_input():
    floor = int(input("Please select floor 1-4:  "))
    for (floor >= 5 or floor <=0) :
        print("floor not available")
        floor = int(input("Please select floor 1-4:  "))
    return floor


def move_up():
    global floor_select
    global current_floor
    global log_list
    while floor_select >= current_floor :
        print ("You are currently on floor:  " + str(current_floor))
        log_list.append(current_floor)

        if floor_select == current_floor:
            print ("You have arrived at floor " + str(current_floor))
            floor_select = get_input()
            print(log_list)
            current_floor += 1

def move_down():
    global floor_select
    global current_floor
    global log_list
    while floor_select < current_floor:
        current_floor -= 1
        print ("You are currently on floor:  " + str(current_floor))
        
        if floor_select == current_floor:
            print ("You have arrived at floor " + str(current_floor))
        if floor_select >= 5:
            print ("floor is not available")
        print(log_list)

if __name__ == "__main__":
    current_floor = 1
    floor_select = get_input()
if floor >=5:
    print("floor is not available")
if floor_select >= current_floor :
    move_up()
else:


    move_down()
    