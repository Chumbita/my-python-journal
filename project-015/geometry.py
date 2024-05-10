import math

def calculateCircleArea(ratio):
  return math.pi * ratio**2

def calculateCylinderVolume(ratio, h):
  return calculateCircleArea(ratio) * h

print("-----|CIRCULE AREA AND CYLINDRE VOLUME|-----\n1) Circle Area.\n2) Cylinder Volume")
user_option = int(input("\nChoose the option: "))
if user_option == 1: 
  input_ratio = float(input("Enter the radius of the circle: "))
  result = calculateCircleArea(input_ratio)
  print(f"A= {result:.2f} units^2")
elif user_option == 2:
  input_ratio = float(input("Enter the radius of the cylinder:  "))
  input_height = float(input("Enter the height of the cylinder: "))
  result = calculateCylinderVolume(input_ratio, input_height)
  print(f"V= {result:.2f} units^3")