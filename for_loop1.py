def mul():
    n = int(input("Enter the number:"))
    for i in range(1,16):
        k = n*i
        print(n,"*",i,"=",k)
if __name__ == "__main__":
    mul()