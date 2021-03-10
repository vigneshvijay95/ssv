# kilometer converts into miles
def user_input():
    kilometers = float(input("Enter the kilometers: "))
def calc():
    conv_fact = 0.621371
    miles = kilometers * conv_fact
    print('%0.3f kilometers is equal to %0.3f miles'%(kilometers,miles))
if __name__ == "__main__":
    user_input()
    calc()