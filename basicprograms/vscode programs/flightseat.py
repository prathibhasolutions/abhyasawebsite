class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.capacity > len(self.passengers):
            self.passengers.append(name)
            print("passenger added")
        else:
            print("Flight is full")
    

flight1 = Flight(5)
flight2 = Flight(8)
flight3 = Flight(2)

number = int(input("How many passengers do you want to add: "))

while True:
    name = input("passenger name: ")
    flightnumber = int(input("flight number: "))
    if flightnumber == 1:
        flight1.add_passenger(name)
    elif flightnumber == 2:
        flight2.add_passenger(name)
    elif flightnumber == 3:
        flight3.add_passenger(name)

        
