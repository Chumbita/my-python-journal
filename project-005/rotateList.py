def rotateList(list, n):
  a = len(list) - n
  new_list = list[a:]
  new_list += list[0:a]
  
  return new_list

list = [1, 2, 3, 4, 5]
print(list)
list = rotateList(list, 2)
print(list)