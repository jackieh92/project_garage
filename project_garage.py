# jh
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
        print("Welcome, here is your ticket")
        for ticket in self.tickets:
            print(ticket)
        self.tickets -=1 
        self.parkingSpaces -=1

# aa

    # Method payForParking, where customer pays for parking
    def payForParking(self, time, paid):
        time = int(input("How many hours will you park here?"))
        self.currentTicket[paid] = time
        while True:
            if self.paid == 0:
                print(f"You owe {self.paid} when you leave")
            elif self.paid != 0:
                print("Your ticket has been paid. You have 15 minutes to leave")
                self.paid == True

    # Method leaveGarage, where customer leaves
    def leaveGarage(self):
        while True:
            if self.paid == 0:
                input(f"Please pay {self.time}")
                del self.currentTicket[paid]
            else:
                print("Thank you, have a nice day")
                break
        self.tickets +=1 
        self.parkingSpaces +=1

# jh

# Method that instantiates Garage class
def run():
    soCheesyGarage = Garage([],[],{})
    while True:
        response = input("what would you like to do? Your options are park, pay or leave")
        if response.lower() == "park":
            soCheesyGarage.takeTicket()
        if response.lower() == "pay":
            soCheesyGarage().payForParking()
        if response.lower() == 'leave':
            soCheesyGarage().leaveGarage
            break


run()

