# Didn't like this code and figured that it'd be most appropriate to just use Mr.M's as my format and just change the data
class Cringekid:
    def __init__(self, age = 0):
         self._age = age
      
    def get_age(self):
        return self._age
      
    def set_age(self, x):
        self._age = x
  
jason = Cringekid()
  
jason.set_age(16)
  
print(jason.get_age())
  
print(jason._age)
