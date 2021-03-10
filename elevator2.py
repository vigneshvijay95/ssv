class elevator:
    def __init__ (self,floor_select,current_floor,log_list):
        self.floor_select = floor_select
        self.current_floor = current_floor
        self.log_list = log_list
        floor_select = int(input("Please select floor 1-4:  "))
        current_floor = 1
        log_list=[]
        def elevator_movesup():
             while floor_select > current_floor:
                current_floor += 1
                print ("You are currently on floor:  " + str(current_floor))
                log_list.append(floor_select)
                if floor_select == current_floor:
                    print ("You have arrived at floor " + str(current_floor))
                    floor_select = int(input("Please select floor 1-4:  "))
                    print(" Log list:", log_list)
                    def elevator_movesdown():
                        while floor_select < current_floor:
                            current_floor -= 1
                            print ("You are currently on floor:  " + str(current_floor))
                            if floor_select == current_floor:
                                print ("You have arrived at floor " + str(current_floor))
                                if "__floor_select__" = "__current_floor__":
                                    if floor_select = 


             
