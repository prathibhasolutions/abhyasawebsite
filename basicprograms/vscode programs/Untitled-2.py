class Bus:
    def _init_(self, seats):
        self.seats = seats
        self.passengers=[]
    def add_passenger(self,name):
        if self.seats > len(self.passenger):
           self.passenger.append(name)
           print(f"{name} seat is booked")
        else:
           print(f"{name}, there is no seat")  
bus = Bus(3)
for name in range(3):
    name = input("passenger name :")


    print(name)            
    