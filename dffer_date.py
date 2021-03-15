from datetime import date
def datetime():
    f_date = date(1995, 8, 8)
    l_date = date(2021, 8, 8)
    delta = l_date - f_date
    print(delta.days)
if __name__ == "__main__":
    datetime()
