from ticket_type import *
from sportsticket import *
from liveperformanceticket import *
from json_file_manager import *


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty")


def create_ticket(ticket_type):

    print("\nEnter the ticket details\n")

    event_name = get_non_empty("Enter event name: ")
    event_time = input("Enter event time (dd/mm/yyyy hh:mm): ")
    venue = input("Enter event venue: ")
    price = float(input("Enter ticket price: "))
    total_tickets = int(input("Enter number of tickets available: "))

    # ---------------------SPORTS---------------------------
    if ticket_type == Ticket_Type.SPORT:

        while True:
            try:
                print("Select one of the following sports [1-6]: ")
                sport_choice = int(input(
                    "\t[1]Football\n\t[2]Rugby\n\t[3]GAA\n\t[4]Golf\n\t[5]F1\n\t[6]Boxing\n"
                ))
            except ValueError as error:
                print(f"Invalid Input. {error} is not a number!")
            else:
                if sport_choice == 1:
                    sportStr = "Football"
                    break # valid input recieved and it stops asking - terminates loop
                elif sport_choice == 2:
                    sportStr = "Rugby"
                    break
                elif sport_choice == 3:
                    sportStr = "GAA"
                    break
                elif sport_choice == 4:
                    sportStr = "Golf"
                    break
                elif sport_choice == 5:
                    sportStr = "F1"
                    break
                elif sport_choice == 6:
                    sportStr = "Boxing"
                    break
                else:
                    print("Invalid choice. Try again.")

        competition = input("Enter competition name: ")

        sports_ticket = SportsTicket(
            event_time, event_name, venue, price, total_tickets, sportStr, competition
        )

        print("\nThe details of the ticket created are:\n")
        print(sports_ticket) # when this is called -> sports_ticket.__str__() is called

        JSONFileManager.WriteObjectToJSONFile(
            "sportstickets.json",
            sports_ticket.getObjectData() #converts object into a dict 
        )
        # takes input from user, creates an object, displays it then stores it to json 

    # ---------------------PERFORMANCE---------------------------
    elif ticket_type == Ticket_Type.PERFORMANCE:

        while True:
            try: #code that might fail
                print("Select one of the following live performance categories [1-4]: ")
                performance_choice = int(input(
                    "\t[1]Concert\n\t[2]Musical\n\t[3]Play\n\t[4]Standup Comedy\n"
                ))
            except ValueError as error:
                print(f"Invalid Input. {error} is not a number!")
            else:
                if performance_choice == 1:
                    performance_type = "Concert"
                    break
                elif performance_choice == 2:
                    performance_type = "Musical"
                    break
                elif performance_choice == 3:
                    performance_type = "Play"
                    break
                elif performance_choice == 4:
                    performance_type = "Standup Comedy"
                    break
                else:
                    print("Invalid choice. Try again.")

        performance_ticket = LivePerformanceTicket(
            event_time, event_name, venue, price, total_tickets, performance_type
        )

        print("\nThe details of the ticket created are:\n")
        print(performance_ticket)

        JSONFileManager.WriteObjectToJSONFile(
            "performancetickets.json",
            performance_ticket.getObjectData()
        )


def view_tickets(ticket_type):

    if ticket_type == Ticket_Type.SPORT:
        tickets = JSONFileManager.LoadObjectsFromJSONFile(
            "sportstickets.json", SportsTicket
        )
    elif ticket_type == Ticket_Type.PERFORMANCE:
        tickets = JSONFileManager.LoadObjectsFromJSONFile(
            "performancetickets.json", LivePerformanceTicket
        )

    print("\nTickets:\n")

    for ticket in tickets:
        print(ticket)
        print("----------------------------------")


def search_tickets(ticket_type):

    search_name = input("Enter event name to search: ")

    if ticket_type == Ticket_Type.SPORT:
        tickets = JSONFileManager.LoadObjectsFromJSONFile(
            "sportstickets.json", SportsTicket
        )
    elif ticket_type == Ticket_Type.PERFORMANCE:
        tickets = JSONFileManager.LoadObjectsFromJSONFile(
            "performancetickets.json", LivePerformanceTicket
        )

    found = False

    for ticket in tickets:
        if ticket.getEventName().lower() == search_name.lower():
            print("\nTicket Found:\n")
            print(ticket)
            found = True

    if found == False:
        print("No matching ticket found.")


def adminmenu():
    flag = True

    while flag:
        print("""\n Please choose one from the following options:
        [1] Create New Sports Ticket
        [2] Create New Live Performance Ticket
        [3] View All Sports Tickets
        [4] View All Live Performance Tickets
        [5] Search Sports Tickets
        [6] Search Live Performance Tickets
        [7] Exit the Application\n""")

        try:
            choice = int(input("Please Enter your Selection [1-7]: "))
        except ValueError as error:
            print(f"Invalid Input. {error} is not a number!")
        else:
            if choice == 1:
                create_ticket(Ticket_Type.SPORT)
            elif choice == 2:
                create_ticket(Ticket_Type.PERFORMANCE)
            elif choice == 3:
                view_tickets(Ticket_Type.SPORT)
            elif choice == 4:
                view_tickets(Ticket_Type.PERFORMANCE)
            elif choice == 5:
                search_tickets(Ticket_Type.SPORT)
            elif choice == 6:
                search_tickets(Ticket_Type.PERFORMANCE)
            elif choice == 7:
                print("\nExiting the application...GoodBye!\n\n")
                flag = False
            else:
                print(f"Invalid selection. {error} Please try again!")

    # using *args - used
    # read in from existing json file 
    # create objects from said file 
    # know how to use get obj data 
    # implementing an interface - idata 
    # data validation - evaluate input -> has to have a reply ->if statement 
    # int, float, empty str 
    # taking multiple argumnets 
    # tickets should be in float 
    # validation for empty string