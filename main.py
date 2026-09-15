import json 
from sportsticket import *
from liveperformanceticket import * 
from menu import adminmenu

adminmenu() # UI entry point
sports_ticket1 = SportsTicket("11/02/2024 15:00", "Ireland vs. Italy", "Aviva Stadium Dublin", 120, 51700, "Rugby", "2024 Six Nations Championship")
print(sports_ticket1.__str__()) #creates ticket manually. 

sports_ticket1.sellTickets() # verifies ticket count decreases (state mutation + validation)
print("No. Tickets Available: "+str(sports_ticket1.getNoTicketsAvailable()))

with open("sportstickets.json","r") as sports_tickets_file:
    sports_tickets_data = json.load(sports_tickets_file)

sports_tickets_data_s = json.dumps(sports_tickets_data)
sports_ticket2 = json.loads(sports_tickets_data_s, object_hook= SportsTicket) # for every dict call sportsticket(dict)

print(sports_ticket2[0])

sports_ticket2[0].sellTickets()

print("No. Tickets Available: "+str(sports_ticket2[0].getNoTicketsAvailable()))

performance_ticket1 = LivePerformanceTicket("21/02/2023 20:00", "Andre Rieu", "3 Arena Dublin", 68.30, 8000, "Concert")
print(performance_ticket1.__str__())

performance_ticket1.sellTickets()
print(performance_ticket1.__str__())

print("No. Tickets Available: "+ str(performance_ticket1.getNoTicketsAvailable()))

with open("performancetickets.json", "r") as performance_tickets_file:
    performance_tickets_data = json.load(performance_tickets_file)

performance_tickets_data_s = json.dumps(performance_tickets_data)
performance_tickets2 = json.loads(performance_tickets_data_s, object_hook= LivePerformanceTicket)

print(performance_tickets2[0])
performance_tickets2[0].sellTickets()
print("No. Tickets Available: "+ str(performance_tickets2[0].getNoTicketsAvailable()))

# sports_ticket.getObjectData() -> dict = Serialisation
# json.dump() -> file =

#                 Decerialisation (obj hook)
# sports_tickets_data = json.load(file) = [
# {"event name: ....", "sport", "Rubgy"}] -> these are plain dictionaries   -> list of dicts raw rata, no behavior key-value storage
# sports_tickets_data[0].sellTickets()  # ❌ dict has no method

# Purpose of obj hook -> automatically called for every dict decoded from json 
# dict -> custom object 

#sports_ticket2 = json.loads(   -> lists of SportsTicket objects, data and behaviour 
#    sports_tickets_data_s,
#    object_hook=SportsTicket)
# what this means = [{"event_name: "Ireland vs Italy, "sport": "Rugby"}]

# json.dumps(...)
# json.loads(..., object_hook=...)
