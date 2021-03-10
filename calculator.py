
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def init():
    print("Select operation")
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. divide")
    choice = input("enter the  choice:")
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))

    if choice == '1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=",multiply(num1,num2)) 
    elif choice == '2':
        print(num1,"/",num2,"=",divide(num1,num2)) 
    else:
        print ("invalid input")
if __name__ == "__main__":
    init()

 


   

