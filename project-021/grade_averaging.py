import os
notas = {"Mario Carriz": [1,2,3],"Chumbita Luciano": [4,5,6]}

def upload_notes():
  flag = True
  scores = []
  print("-----|UPLOAD NOTES|-----\n")
  a = int(input("Enter the amounts of evaluative grades your course has: "))
  while flag:
    os.system('cls')
    print("-----|UPLOAD NOTES|-----\n")
    student_name = input("Studen Name: ")
    for i in range(a):
      x = float(input(f"Score {i+1}: "))
      scores.append(x)
    notas[student_name] = scores

    print("\nStudeny and scores uploaded successfully.")
    opc = input("\nDo you want to add another student? Y/N format: ")
    if opc == "N":
      flag = False
    else:
      print("ERROR. Invalid Option.")

def show_notes():
  if notas: 
    f_s = notas.keys()
    notes_amount = len(notas[f_s[0]])
    text = f"{'STUDENT':<20}"
    for i in range(notes_amount - 1):
      text += f'NOTA {i} '
    print(text)

    for s in notas.keys():
      txt_input = f'{s:<21}'
      for a in notas[s]:
        txt_input += f'{a:<6}'
      print(txt_input)
  
def main():  
  print("-----|UNIVERSITY SYSTEM|-----\n-1) UPLOAD COURSE NOTES.\n-2) SHOW COURSE NOTES.\n.3) CALCULATE AVERAGE.\n-4) EXIT.")
  operation = int(input(f"Choose an operation: "))
  os.system('cls')
  if operation == 1:
    upload_notes()
  elif operation == 2:
    show_notes()
  # elif operation == 3:
  #   average_notes()
  else:
    print("ERROR. Invalid Operation.")
  input("\nPRESS ENTER TO CONTINUE...")

if __name__ == '__main__':
  main()  
