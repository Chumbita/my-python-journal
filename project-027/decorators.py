class User:
  def __init__(self, username, password):
    self._username = username # protected
    self.__password = password # private

  @property
  def username(self):
    return self._username
  
  def set_username(self, value):
    self._username = value

  @property
  def password(self):
    return self.__password
  
  def set_password(self, value):
    self.__password = value

user1 = User("charlygarcia_ofc", "noautostune")

print(user1.username)
user1.set_username("charlygarcia.ok")
print(user1.username)

print(user1.password)
user1.set_password("nollueveescupen")
print(user1.password)

# print(user1.__password) devuelve error.