def insert():
    l = []
    for x in range (500,600):
        if (x%5==0) and (x%7==0):
            l.append(str(x))
    print(','.join(l))
if __name__ == "__main__":
    insert()