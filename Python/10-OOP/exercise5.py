class Train:
    def book_ticket(self):
        print("your ticket is booking....")
    def get_status(self):
        print("your ticket has been booked")
    def get_information(self):
        print("your train will arriving monday at 5 am")

passanger = Train()
passanger.book_ticket()
passanger.get_status()
passanger.get_information()
