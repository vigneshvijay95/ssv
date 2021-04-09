def insert():
    num = int(input("Enter the multiplication table:"))
    for i in range(1,16):
        print(num,'x',i,'=',num*i)
if __name__== "__main__":
    insert()