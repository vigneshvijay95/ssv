def init():
    a = "vignesh is a good boy"
    b = "He is be holder"
    c = a + " "+b
    quantity = 3
    itemno = 547
    price = 50.00
    myorder = "i want {2} dollars of {0} pieces of item {1}."
    print(myorder.format(quantity,itemno,price))
    print (a)
    print(len(a))
    print(a[3:10])
    print(a[:11])
    print(a[2:])
    print(a[-3:-10])
    print(a.upper())
    print(a.lower())
    print(a.strip())
    print(a.replace("is","was"))
    print(c)
    if "good" in a:
        print("yes good is present in a")
    else:
        print("good is not present in a")

if __name__ == "__main__":
    init()