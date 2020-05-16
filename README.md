# Project Garage

Project Garage is the first back-end awesome program developed by SoCheese. Hope you like it (:

Please find program requirenments [here.](https://classroom.google.com/c/OTQ5OTQ1MDk1MDNa/a/MTAyODI1MDQzNjU4/details)

### takeTicket & run()

_Code by Jackie H._

Class *Garage* is initialized with positional arguments:

* tickets
* parkingSpaces
* currentTicket

To follow best-pracitses, a doc-string and comments have been added. 

Method *takeTicket* instantiates Garage class and allows the user to interact with the program.

*run()* prompts users with questions and calls takeTicket, payForParking, currentTickets to execute methods.

### payForParking & leaveGarage

_Code by Aaron A._

Method *payForParking* allows customers to pay for parking. Method asks for input for amount of time, and updates "paid" key in currentTicket dictionary.

Current version of code only accepts promocode 'pay' as payment method.

In addition, method provides message to user that have paid to leave garage in 15 minutes. 

Method *leaveGarage* on the other hand, allows customer to checkout from garage, thanks customers who paid and increases ticket and space availability by updating parkingSpaces and tickets lists. 