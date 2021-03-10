def user_input():
    values = (input("enter the values:"))
    list = values.split(",")
    Tuple = tuple(list)
    print('List :',list)
    print('Tuple :',tuple)
if __name__ == "__main__":
    user_input()   