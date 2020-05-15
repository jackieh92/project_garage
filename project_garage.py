class Garage():
    
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

        """
            Garage requires 3 positional arguments:
            -tickets: expects ints and is a list
            -parkingSpaces: expects ints and is a list
            -currentTicket: expects ints and is a dictionary
        """

    # Method where the customer take ticket out of the machine - jh
    def takeTicket(self):
        print("\n* Welcome, here is your ticket.\n")
        self.tickets.pop(-1)
        self.parkingSpaces.pop(-1)

# aa

    # Method payForParking, where customer pays for parking
    def payForParking(self):
        time = int(input("\n* For how many hours?\n"))
        cost = 2 * time
        self.currentTicket[cost] = time
        while True:
            if not cost:
                print(f"\n* You owe {time} hours\n")
            elif cost != 0:
                print("\n* Your ticket has been paid. You have 15 minutes to leave\n")
                cost == True
                break

    # Method leaveGarage, where customer leaves
    def leaveGarage(self):
        while True:
            if self.currentTicket == 0:
                input(f"\n* Please pay {self.time}.\n")
                del self.currentTicket[paid]
            else:
                print("\n* Thank you, have a nice day!\n")
                break
        self.tickets.append(self.currentTicket)
        self.parkingSpaces.append(self.currentTicket)

# jh

# Method that instantiates Garage class
def run():
    soCheesyGarage = Garage([1, 2, 3, 4], [1, 2, 3, 4], {})
    while True:
        response = input("\n* What would you like to do? 'park', 'pay' or 'leave'? \n")
        if response.lower() == "park":
            soCheesyGarage.takeTicket()
        if response.lower() == "pay":
            soCheesyGarage.payForParking()
        if response.lower() == 'leave':
            soCheesyGarage.leaveGarage()
            break

run()