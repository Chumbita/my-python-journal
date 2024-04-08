def unionAndDiference(list_1, list_2):
  x = list_1 | list_2 # list_1.union(list_2) #list_1.update(list_2)
  y = list_1 & list_2 # list_1.intersection(list_2)
  z = list_1 - list_2 # list_1.difference(list_2)
  z.update(list_2 - list_1)

  print(f"-Lists: 1. {list_1} AND 2. {list_2}\n-Union: {x}\n-Intersection: {y}\n-Difference: {z}")

my_list1 = {1, 2, 3, 4}
my_list2 = {3, 4, 5, 6}

unionAndDiference(my_list1, my_list2)