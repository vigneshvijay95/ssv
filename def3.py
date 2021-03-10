def hcf(a,b):
    if a>b:
        smaller = a
    else:
        smaller = b
        for i in range(1,smaller + 1):
            if((a % i == 0)and(b % i ==0)):
                hcf = i
                return hcf
def u_input():
    a =int(input("Enter first number:"))
    b =int(input("Enter second number:"))
    print("hcf of the two number",a ,"and",b,"is",hcf(a,b))
if __name__ == "__main__":
    u_input()