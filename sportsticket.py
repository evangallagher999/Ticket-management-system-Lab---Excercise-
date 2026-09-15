from ticket import *
from idata import *
from sport import *

class SportsTicket(Ticket, IData):
    def __init__(self, *args): #*agrs can be called anything, *agrs used to create flexabilty
        if len(args) > 1: #manual input 
            event_time = args[0] #key pairings, tuple and ordered immutable list
            event_name = args[1] # effectivley a method overloading where the same method can accept different numbers and kinds of parametes. 
            venue = args[2]
            price = args[3]
            total_tickets = args[4]
            sportStr = args[5]
            competition = args[6] 
        elif len(args) == 1: #json input
            event_time = args[0].get('event_time') # accesses values inside the dict
            event_name = args[0].get('event_name')
            venue = args[0].get('venue')
            price = args[0].get('price')
            total_tickets = args[0].get('total_tickets')
            sportStr = args[0].get('sport')
            competition = args[0].get('competition')

        sport = Sport.FOOTBALL #string into enum instead of the opposite way 
                                # moved string outside of if statement, otherwise wouldnt run  as >1 

        if sportStr == "Football":
                sport = Sport.FOOTBALL
        elif sportStr == "Rugby":
                sport = Sport.RUGBY
        elif sportStr == "GAA":
                sport = Sport.GAA
        elif sportStr == "Golf":
                sport = Sport.GOLF
        elif sportStr == "F1":
                sport = Sport.F1
        elif sportStr == "Boxing":
                sport = Sport.BOXING

        super().__init__(event_time, event_name, venue, price, total_tickets)
        self.__sport = sport # not inharited 
        self.__competition = competition 

    def getSport(self):
        return self.__sport
    
    def setSport(self, sport):
        self.__sport = sport

    def getCompetition(self):
        return self.__competition
    
    def setCompetition(self, competition):
        self.__competition = competition

    def __str__(self):
        sportStr = ""

        if self.__sport == Sport.FOOTBALL: #enum to string. used to display to user, saved to python
            sportStr = "Football"
        elif self.__sport == Sport.RUGBY:
            sportStr = "Rugby"
        elif self.__sport == Sport.GAA:
            sportStr = "GAA"
        elif self.__sport == Sport.GOLF:
            sportStr = "Golf"
        elif self.__sport == Sport.F1:
            sportStr = "Formula 1 Racing"
        elif self.__sport == Sport.BOXING:
            sportStr = "Boxing"

        return f"""Sports Ticket Details:\n\tName: {self._event_name}
        Date & Time: {self._event_time} 
        Venue: {self._venue}\n\tPrice: {self._price}\n\tSport: {sportStr}
        Competition: {self.__competition}
        No. Tickets Sold: {self._total_tickets-self._no_tickets_available}"""
    
    def getObjectData(self): # had it as pass now gonna fill out pg22
        
        return{
            "event_name": self._event_name,
            "event_time": self._event_time.strftime("%d/%m/%Y %H:%M"),
            "venue": self._venue,
            "price": self._price,
            "total_tickets": self._total_tickets, 
            "sport": self.__convertSportEnumToStr(), 
            "competition":self.__competition
        }
    
    def __convertSportEnumToStr(self): # do same for performance ticket
        sportStr = ""
        if self.__sport == Sport.FOOTBALL:
            sportStr = "Football"
        elif self.__sport == Sport.RUGBY:
            sportStr = "Rugby"
        elif self.__sport == Sport.GAA:
            sportStr = "GAA"
        elif self.__sport == Sport.GOLF:
            sportStr = "Golf"
        elif self.__sport == Sport.F1:
            sportStr = "Formula 1 Racing"
        elif self.__sport == Sport.BOXING:
            sportStr = "Boxing"

        return sportStr
    
