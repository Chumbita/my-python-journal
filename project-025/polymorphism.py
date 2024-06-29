class Animal: 
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    pass

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed
  
  def make_sound(self):
    return f"{(self.name).upper()}: ¡GUAU GUAU!"

class Cat(Animal):
  def __init__(self, name, colour):
    super().__init__(name)
    self.colour = colour
  
  def make_sound(self):
    return f"{(self.name).upper()}: ¡MIAU MIAU!"
  
dog1 = Dog("Loki", "Dogo Argentino")
cat1 = Cat("Yummi", "White")

print(dog1.make_sound())
print(cat1.make_sound())