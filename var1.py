x = "vignesh"
y = "Hai Welcome "
print (x+y)
# variable declare by using value to concat
x = 15
y = 25
z = x+y
print(z)
# variable declare a global and local
x = "fantastic"
y = "hai welcome"
def init():
    global x # global keyword is used to change allready
    global y
    x = "super"
    y = "python is fantastic language"
    z = x+y
    print (z)
    return x
    return y
if __name__ == "__main__":
    init()
    print(x)
    print(y)