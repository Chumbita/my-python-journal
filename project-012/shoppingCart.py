import os

shoppingCart = dict()
flag = True

def shoppingCartList(dictionary):
  total = 0
  print("-----|YOU SHOPPING CART|------\n")
  for x, y in dictionary.items():
    print(f"{x}: {y[1]} * ${y[0]} = ${float(y[0]) * int(y[1])}")
    total += float(y[0]) * int(y[1])
  print(f"\nTOTAL: ${total}")

while flag: 
  user_response = False
  print("-----|SHOPPING CART|------")
  u_input_product = input("-Product: ")
  u_input_price = input("-Price: ")
  u_input_amount = input("-Amount: ")
  
  shoppingCart[u_input_product] = [u_input_price, u_input_amount]
  while not user_response:
    u_input_continue = input("\nAdd another product? Type YES/NO format: ")
    if u_input_continue == "YES": 
      flag = True
      user_response = True
      os.system("cls")
    elif u_input_continue == "NO":
      flag = False
      user_response = True
      os.system("cls")
    else: 
      print("Invalid option!") 

shoppingCartList(shoppingCart)