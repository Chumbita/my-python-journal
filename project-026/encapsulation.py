class User:
  def __init__(self, username, password):
    self._username = username # protected
    self.__password = password # private

  def get_username(self):
    return self._username
  
  def set_username(self, value):
    self._username = value

  def get_password(self):
    return self.__password
  
  def set_password(self, value):
    self.__password = value

user1 = User("charlygarcia_ofc", "noautostune")

print(user1.get_username())
user1.set_username("charlygarcia.ok")
print(user1.get_username())

print(user1.get_password())
user1.set_password("nollueveescupen")
print(user1.get_password())

# print(user1.__password) devuelve error.