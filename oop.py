# ============== Task 1 ================ 
class Vehicle:
  def __init__(self, registration_number, type, owner):
    self.registration_number = registration_number
    self.type = type
    self.owner = owner
    
  def update_owner(self, new_owner):
     self.owner = new_owner
     
     
v1 = Vehicle('1230', 'Sedan', 'John Doe')
v2 = Vehicle('4423', 'SUV', 'Michael')     

print(v1.registration_number)
print(v1.type)
print(f"Owner: {v1.owner}")

v1.update_owner('Ricardo')
print(f"New owner: {v1.owner}")



# ============== Task 2 ================ 
class Event:
  num_of_participants = 0
  
  def __init__(self, name, date, participants):
    self.name = name
    self.date = date
    self.participants = participants
    Event.num_of_participants += self.participants
    
  def get_participant_count():
    return Event.num_of_participants
  
    
e1 = Event('Moon Landing', 'Jul 20, 1969', 200)
e2 = Event('Facebook Launch', 'Feb 4, 2004', 1200)    
e3 = Event('Twitter Launch', 'March 21, 2006', 2300)

print("Total participants ==> {} ".format(Event.get_participant_count())) # Expected output = 3700