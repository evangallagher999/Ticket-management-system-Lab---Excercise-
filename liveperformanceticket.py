from ticket import *
from idata import * 
from performance_type import * 

class LivePerformanceTicket(Ticket, IData):
    def __init__(self, *args): #*agrs can be called anything
        if len(args) > 1: 
            event_time = args[0] #key pairings
            event_name = args[1]
            venue = args[2]
            price = args[3]
            total_tickets = args[4]
            performance_typeStr = args[5]
        elif len(args) == 1:
            event_time = args[0].get('event_time')
            event_name = args[0].get('event_name')
            venue = args[0].get('venue')
            price = args[0].get('price')
            total_tickets = args[0].get('total_tickets')
            performance_typeStr = args[0].get('performance_type')
            

        performance_type = Performance_Type.CONCERT #string into enum instead of the opposite way
        performance_TypeStr =""
        if performance_TypeStr == "Concert": # small to Capital 
                performance_type = Performance_Type.CONCERT
        elif performance_TypeStr == "Musical":
                performance_type = Performance_Type.MUSICAL
        elif performance_TypeStr == "Play":
                performance_type = Performance_Type.PLAY
        elif performance_TypeStr == "Standup Comedy":
                performance_type = Performance_Type.STANDUP_COMEDY



        super().__init__(event_time, event_name, venue, price, total_tickets)
        self.__performance_type = performance_type # not inharited 
         
    def getPerformanceType(self):
        return self.__performance_type
    
    def setPerformanceType(self, performance_type):
        self.__performance_type = performance_type

    def __str__(self):
    
        return f"""Live Performance Ticket Details: \n\tName: {self._event_name}
        \n\tDate & Time: {self._event_time}
        \n\tVenue:  {self._venue}
        \n\tPrice: {self._price}
        \n\tPerformance Type: {self.__convertPerfromanceEnumToStr()}
        \n\tNo. Tickets sold: {self._total_tickets - self.getNoTicketsAvailable()}""" 
    
    def computePrice(self):
        pass
    
    def getObjectData(self):
        return{
            "event_name": self._event_name,
            "event_time": self._event_time.strftime("%d/%m/%Y %H:%M"),
            "venue": self._venue,
            "price": self._price,
            "total_tickets": self._total_tickets, 
            "performance_type": self.__convertPerfromanceEnumToStr()
        }
        

    def __convertPerfromanceEnumToStr(self): # converts enum to string
        performance_TypeStr = ""
        if self.__performance_type == Performance_Type.CONCERT:
            performance_TypeStr  = "Concert"
        elif self.__performance_type == Performance_Type.MUSICAL: 
            performance_TypeStr = "Musical"
        elif self.__performance_type == Performance_Type.PLAY:
            performance_TypeStr = "Play"
        elif self.__performance_type == Performance_Type.STANDUP_COMEDY:
            performance_TypeStr = "Standup Comedy"
        
        return performance_TypeStr # internal (enum) -> string (json/display)



            # given code to json 
            # 2 json 
            # json file manager given 
            # json file manager and arguments *args read in attrivutes from json file given into constructor, display on screen, add to file. 
            # abstract classes & interface implementation 
            # enum to string -> str to enum 
            