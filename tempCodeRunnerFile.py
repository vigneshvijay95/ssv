
    if option == "1":
        classType = BookingClass.FIRSTCLASS
        otherTyes.append(BookingClass.BUSINESS)
        otherTyes.append(BookingClass.ECONOMY)
    elif bClass == "2":
        classType = BookingClass.BUSINESS