# Query: ass1.py
# ContextLines: 1

import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("WELCOME TO AIR LINES BOOKING:")


class BookingClass:
    ECONOMY = 'Economy'
    BUSINESS = 'Business'
    FIRSTCLASS = 'Firstclass'


class Seat:
    def __init__(self, row_number: int, letter: str):
        self.row_number = row_number
        self.letter = letter

    def __str__(self):
        return '{}{}'.format(self.row_number, self.letter)


class SeatingArea:
    def __init__(self, booking_class: str, start_row: int, row_count: int, seats_per_row: int):
        self.booking_class = booking_class
        self.seat_count = row_count * seats_per_row
        self.seats_remaining = []

        for row_number in range(start_row, row_count + start_row):
            for seat_number in range(seats_per_row):
                new_seat = Seat(row_number, letters[seat_number])
                self.seats_remaining.append(new_seat)


class Flight:
    def __init__(self, economy_seats: SeatingArea, business_seats: SeatingArea, firstClass_seats: SeatingArea):
        
        self.seating_areas = {
            BookingClass.ECONOMY: economy_seats,
            BookingClass.BUSINESS: business_seats,
            BookingClass.FIRSTCLASS: firstClass_seats}

    def print_statistics(self):
        for booking_class, seating_area in self.seating_areas.items():
            print('{}: {}% available'.format(
                booking_class,
                len(seating_area.seats_remaining) / seating_area.seat_count * 100))

    def remaining_seat_count(self, booking_class: str):
        return len(self.seating_areas[booking_class].seats_remaining)

    def get_seat(self, booking_class: str):
        return self.seating_areas[booking_class].seats_remaining.pop()


class Passenger:
    def __init__(self, name: str):
        self.name = name
        self.booking_id = None
        self.seat = None

    def has_booked(self):
        return self.booking_id is not None

    def book(self, flight: Flight, booking_class: str):
        if flight.remaining_seat_count(booking_class) != 0:
            self.seat = flight.get_seat(booking_class)
            self.booking_id = random.Random().randrange(1000, 10000)
            return True

        return False



def main():
    firstClass = SeatingArea(BookingClass.FIRSTCLASS, start_row=1, row_count=5, seats_per_row=1)
    business = SeatingArea(BookingClass.BUSINESS, start_row=6, row_count=5, seats_per_row=2)
    economy = SeatingArea(BookingClass.ECONOMY, start_row=11, row_count=5, seats_per_row=3)
    flight = Flight(economy, business, firstClass)

    john = Passenger('John')
    john.book(flight, BookingClass.ECONOMY)
    print(john.seat)
    print(john.booking_id)

    flight.print_statistics()


if __name__ == '__main__':
    main()
