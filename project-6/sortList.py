def sortListAsc(list):
  for i in range(0, len(list)):
    for j in range(0, len(list) -1):
      if list[j] > list[j+1]:
        x = list[j]
        list[j] = list[j+1]
        list[j+1] = x

def sortListDes(list):
  for i in range(0, len(list)):
    for j in range(0, len(list) -1):
      if list[j] < list[j+1]:
        x = list[j]
        list[j] = list[j+1]
        list[j+1] = x

numbers = [10, 45, 67, 23, 1, 87, 34, 99, 56, 33, 72, 91, 2, 10, 45, 23, 1, 45, 87, 56]
print(f"-Original list: {numbers}")

sortListAsc(numbers)
print(f'-Ascendent sort list: {numbers}')
sortListDes(numbers)
print(f'-Descendent sort list: {numbers}')

