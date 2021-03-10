def u_input():
    num = int(input("enter the number:"))
    if num<0:
        print("Enter the positive number:")
    else:
        sum = 0
        while(num>0):
            sum +=num
            num -=1
            print("The sum of ",sum)
        
if __name__ == "__main__":
    u_input()