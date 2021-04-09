def getInput(flight: Flight):
    classType = None
    name = str(input('Enter the Passanger Name:'))
    option = str(input('Select the Class: \n 1. First Class\n 2. Business Class\n 3. Economy Class'))
    otherTyes = []
    if option == "1":
        classType = BookingClass.FIRSTCLASS
        otherTyes.append(BookingClass.BUSINESS)
        otherTyes.append(BookingClass.ECONOMY)
    elif bClass == "2":
        classType = BookingClass.BUSINESS
        otherTyes.append(BookingClass.FIRSTCLASS)
        otherTyes.append(BookingClass.ECONOMY)
    else:
        classType = BookingClass.ECONOMY
        otherTyes.append(BookingClass.BUSINESS)
        otherTyes.append(BookingClass.FIRSTCLASS

    passenger = Passenger(name)
    while not bookRslt:
        bookRslt = passenger.book(flight, classType)
        if bookRslt:
            print(passenger.seat)
            print(passenger.booking_id)
            break
        else:
            bookRslt = passenger.book(flight, classType)