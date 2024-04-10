import os
clients_DB = {
  "45564667": {
    "name": "Luciano", 
    "lastname": "Chumbita", 
    "adress": "Calle 4", 
    "phone": "3804911112", 
    "mail": "chumbitalexis@gmail.com", 
    "preferential": True}, 
  "21899723": {
    "name": "Mario", 
    "lastname": "Carrizo", 
    "adress": "Calle 2", 
    "phone": "3804911112", 
    "mail": "mariocarrizo@gmail.com", 
    "preferential": True},
  "20301960": {
    "name": "Carlos", 
    "lastname": "Olivera", 
    "adress": "Calle 8", 
    "phone": "3804911112", 
    "mail": "carlosolivera@gmail.com", 
    "preferential": False}
  }

def deleteCliente():
  flag = True
  while flag: 
    os.system("cls")
    print("------|DELETE CLIENT|------")
    nif = input("Enter the customer's NIF number: ")
    if nif in clients_DB.keys():
      clients_DB.pop(nif)
      print("Client successfully eliminated.")
      flag = False
    else: 
      print("The entered NIF number is not recognized as a customer stored in the database.")
      input("PRESS ENTER to continue...")
      

def addCliente():
  new_cliente = dict()
  print("------|ADD ClIENT|------\nEnter the following details:")
  new_client_NIF = input("-NIF: ")
  new_cliente_name = input("-Name: ")
  new_cliente_lastname = input("-Last Name: ")
  new_cliente_adress = input("-Adress: ")
  new_cliente_phone = input("-Phone: ")
  new_client__mail = input("-Email: ")
  new_client__preferential = input("Is a preferred customer? YES/NO: ")
  if new_client__preferential == "YES":
    new_client__preferential = True
  else: 
    new_client__preferential = False
  
  new_cliente[new_client_NIF] = {
    "Name": new_cliente_name,
    "Last Name": new_cliente_lastname,
    "Adress": new_cliente_adress,
    "Phone": new_cliente_phone,
    "Email": new_client__mail,
    "Preferential": new_client__preferential
    }
  clients_DB.update(new_cliente)
  print("\nThe client was added to the database.")

def showCliente():
  print("------|SHOW CLIENT|------")
  nif = input("-Enter the customer's NIF number: ")
  if nif in clients_DB.keys():
    client = clients_DB[nif]
    print(f"""-Name: {client["name"]}\n-Last Name: {client["lastname"]}\n-Adress: {client["adress"]}\n-Phone: {client["phone"]}\n-Email: {client["mail"]}\n-Preferential: {client["preferential"]}""")
  else: 
    print("The entered NIF number is not recognized as a customer stored in the database.")

def shoAllClientes():
  print("------|LIST CLIENTS|------")
  for x in clients_DB.keys():
    print(f"""-NIF: {x}\n-Name: {clients_DB[x]["name"]}\n-Last Name: {clients_DB[x]["lastname"]}\n-Adress: {clients_DB[x]["adress"]}\n-Phone: {clients_DB[x]["phone"]}\n-Email: {clients_DB[x]["mail"]}\n-Preferential: {clients_DB[x]["preferential"]}\n""")

def showAllPreferentsClients():
  print("------|PREFERENTIAL CLIENTS|------")
  for x in clients_DB.keys():
    if clients_DB[x]["preferential"] == True: 
      print(f"""-NIF: {x}\n-Name: {clients_DB[x]["name"]}\n-Last Name: {clients_DB[x]["lastname"]}\n-Adress: {clients_DB[x]["adress"]}\n-Phone: {clients_DB[x]["phone"]}\n-Email: {clients_DB[x]["mail"]}\n-Preferential: {clients_DB[x]["preferential"]}\n""")

def main(): 
  flag = True
  while flag:
    print("------|DATABASE CLIENT MENU------|\n1) Add client.\n2) Delete client.\n3) Show a client.\n4) List all clients.\n5) List all preferentials clients.\n6) Finish.")
    user_opc = int(input("\n-Choose the operation: "))
    os.system("cls")
    if user_opc == 1:
      addCliente()
    elif user_opc == 2:
      deleteCliente()
    elif user_opc == 3: 
      showCliente()
    elif user_opc == 4:
      shoAllClientes()
    elif user_opc == 5:
      showAllPreferentsClients()
    elif user_opc == 6: 
      flag = False
    else: 
      print("Invalid option")
    input("PRESS ENTER to continue...")
    os.system("cls")
  
if __name__ == "__main__":
    main()