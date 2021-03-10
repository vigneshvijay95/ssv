floor_select = int(input("Please select floor 1-4:  "))
current_floor = 1

log_list=[]

if floor_select >= 5 or floor_select <=0:
    print("floor not available")

else:
    while floor_select >= current_floor:
        print ("You are currently on floor:  " + str(current_floor))
        log_list.append(current_floor)

        if floor_select == current_floor:
            print ("You have arrived at floor " + str(current_floor))
            floor_select = int(input("Please select floor 1-4:  "))
            print(log_list)
        current_floor += 1
            
    while floor_select < current_floor:
        current_floor -= 1
        print ("You are currently on floor:  " + str(current_floor))
        

        if floor_select == current_floor:
            print ("You have arrived at floor " + str(current_floor))
        if floor_select >= 5:
            print ("floor is not available")
        print(log_list)
        
    