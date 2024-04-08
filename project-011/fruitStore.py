fruitStock = {
  "Banana": 1.35,
  "Apple": 0.8,
  "Pear": 0.85,
  "Orange": 0.75
  }

flag = True

while flag: 
  print("------|FRUIT STORE|------")
  user_input_fruit = input("Enter the fruit: ")
  if user_input_fruit in fruitStock.keys():
    user_input_n = int(input("Enter the number of kilos: "))
    total = fruitStock[user_input_fruit] * user_input_n
    print(f"Total: ${total}")
    user_input_continue = input("Want to continue? Use the YES/NO format: ")
    if user_input_continue == "NO" or user_input_continue == "YES":
      if user_input_continue == "NO":
        flag = False
    else: 
      print("Invalid option.")
  else: 
    print("The fruit was not found.")