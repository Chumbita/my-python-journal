import os
students_scores = {}

def upload_notes():
  flag = True
  print("-----|UPLOAD NOTES|-----\n")
  amount_notes = int(input("Enter the amounts of evaluative grades your course has: "))
  while flag:
    scores = []
    os.system('cls')
    print("-----|UPLOAD NOTES|-----\n")
    student_name = input("Studen Name: ")
    for i in range(amount_notes):
      x = float(input(f"Score {i+1}: "))
      scores.append(x)
    students_scores[student_name] = scores

    print("\nStudeny and scores uploaded successfully.")
    opc = input("\nDo you want to add another student? Y/N format: ")
    if opc == "N":
      flag = False
    else:
      print("ERROR. Invalid Option.")

def show_notes():
  if students_scores: 
    mykeys = list(students_scores.keys())
    first_student = mykeys[0]
    notes_amount = len(students_scores[first_student])
    txt = f"{'STUDENT':<25}"
    for i in range(notes_amount):
      txt += f'NOTA {i+1} '
    print(txt)

    for student in students_scores.keys():
      txt_input = f'{student:<26}'
      for score in students_scores[student]:
        txt_input += f'{score:<7}'
      print(txt_input)
  else: 
    print("There are nothing to show...")

def average_notes():
  if students_scores: 
    mykeys = list(students_scores.keys())
    first_student = mykeys[0]
    notes_amount = len(students_scores[first_student])
    print(f"{'STUDENT':<25}{'NOTA FINAL'}")

    for student in students_scores.keys():
      txt_input = f'{student:<28}'
      average = 0
      for score in students_scores[student]:
        average += score
      average /= notes_amount
      print(f"{txt_input}{average:.2f}")
  else: 
    print("There are nothing to show...")
  
def main():
  flag = True
  while flag:  
    print("-----|UNIVERSITY SYSTEM|-----\n1) UPLOAD COURSE NOTES.\n2) SHOW COURSE NOTES.\n3) CALCULATE AVERAGE.\n4) EXIT.")
    operation = int(input(f"Choose an operation: "))
    os.system('cls')
    if operation == 1:
      upload_notes()
    elif operation == 2:
      show_notes()
    elif operation == 3:
      average_notes()
    elif operation == 4: 
      flag = False
    else:
      print("ERROR. Invalid Operation.")
    input("\nPRESS ENTER TO CONTINUE...")
    os.system('cls')

if __name__ == '__main__':
  main()  
