import os, math

def seno():
  print("-----|SINE CALCULATOR|-----")
  x = int(input("\nEnter an integer: "))
  print(f"\n{'x':<5} {'sen(x)':<5}\n{'-'*15}")
  for i in range(1, x+1):
    print(f"{i:<5} {math.sin(i):<5.2f}")

def coseno():
  print("-----|COSINE CALCULATOR|-----")
  x = int(input("\nEnter an integer: "))
  print(f"\n{'x':<5} {'cos(x)':<5}\n{'-'*15}")
  for i in range(1, x+1):
    print(f"{i:<5} {math.cos(i):<5.2f}")

def tangente():
  print("-----|TANGENT CALCULATOR|-----")
  x = int(input("\nEnter an integer: "))
  print(f"\n{'x':<5} {'tan(x)':<5}\n{'-'*15}")
  for i in range(1, x+1):
    print(f"{i:<5} {math.tan(i):<5.2f}")
  
def exponencial():
  print("-----|EXPONENTIAL CALCULATOR|-----")
  x = int(input("\nEnter an integer: "))
  print(f"\n{'x':<5} {'e^x':<5}\n{'-'*15}")
  for i in range(1, x+1):
    print(f"{i:<5} {math.exp(i):.2f}")
  
def logaritmo():
  print("-----|NEPERIAN LOGARITHM CALCULATOR|-----")
  x = int(input("\nEnter an integer: "))
  print(f"\n{'x':<5} {'ln(x)':<5}\n{'-'*15}")
  for i in range(1, x+1):
    print(f"{i:<5} {math.log(i):<5.2f}")
  
def main():
  flag = True
  while flag:
    print("-----|SCIENTIFIC CALCULATOR|-----\n\n1)Sin.\n2)Cos.\n3)Tan.\n4)Exponential.\n5)Logarithm.\n6)Get out.\n")
    user_opc = int(input("Choose an operation: "))
    os.system("cls")
    if user_opc == 1:
      seno()
    elif user_opc == 2:
      coseno()
    elif user_opc == 3:
      tangente()
    elif user_opc == 4:
      exponencial()
    elif user_opc == 5: 
      logaritmo()
    elif user_opc == 6:
      flag = False
    else:
      print("Invalid option.")
    input("\nPress ENTER to continue...")
    os.system("cls")

if __name__ == '__main__':
  main()