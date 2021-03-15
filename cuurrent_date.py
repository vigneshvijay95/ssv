import datetime
def current():
    now = datetime.datetime.now()
    print ("current date and time")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
if __name__ == "__main__":
    current()