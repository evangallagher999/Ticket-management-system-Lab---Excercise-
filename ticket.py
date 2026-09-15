from abc import ABC, abstractmethod
import ticketssoldoutexception
# from iprice import * ignore old code 
from datetime import * 
from ticketssoldoutexception import * # get rid of file name before class name 

class Ticket(ABC):#base class  
    def __init__(self, event_time, event_name, venue, price, total_tickets):
        self._event_time = datetime.strptime(event_time, '%d/%m/%Y %H:%M') # strptime -> str > datetime, strftime -> datetime > str
                                                                            # y input 20 -> 2020, Y input = 2020 hour and minutes
        self._event_name = event_name # protected attribute, accesable from child class.  
        self._venue = venue
        self._price = price
        self._total_tickets = total_tickets
        self._no_tickets_available = total_tickets

# Ticket class is abstract, as all subclasses will take its attributes. 
# Ticket is not meant to be used directly, hence the two subclasses. 
# Due to this it is called a Abstract class = cannot be instantiated (cannot create classes from it) & can define abstract methods, (child classes must implement.)
# ABC  - base class for defining Abstract classes, @abstractmethod - decorator marking methods that must be implemented by subclasses. 
# this tells python, this is an abtstract class, do not allow objects of this class to be created. Forcing child classes to implement its own version of __str__(). 


    def getEventTime(self): # Accessor method - access regularly protected/private var. 
        return self._event_time 
    
    def setEventTime(self, event_time): # Mutator method - change what protected/private var
        self._event_time = event_time

    def getEventName(self):
        return self._event_name
    
    def setEventName(self, event_name):
        self._event_name = event_name

    def getVenue(self):
        return self._venue
    
    def setVenue(self, venue):
        self._venue = venue

    def getPrice(self): # limit user input and change
        return self._price
    
    def getTotalTickets(self):
        return self._total_tickets
    
    def setTotalTickets(self, total_tickets):
        self._total_tickets = total_tickets

    def getNoTicketsAvailable(self):
        return self._no_tickets_available
    
    def setNoticketsAvailable(self, no_tickets_available):
        self._no_tickets_available = no_tickets_available


def sellTickets(self): #used for error handling
    try: #code that might fail
        if self._no_tickets_available == 0: # checks for any tickets
            raise TicketsSoldOutException #manually triggers error. 
        self._no_tickets_available -= 1  
        print("Ticket sold successfully") 
    except TicketsSoldOutException: #handle it - error is caught - define controlled behavior
        print("The tickets are sold out for this event")
        return  # ← moved inside except, only returns on error

    @abstractmethod # forces every subclass of Ticket to provide its own implementation of __str__()
    def __str__(self): # everysub class that uses __str__ will have its own print return f string, print statement
        pass 