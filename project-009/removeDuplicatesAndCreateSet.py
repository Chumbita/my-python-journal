def listToSet(a_list):
  x = []
  y = set()

  for i in a_list: 
    if i not in x:
      x.append(i)
  
  y.update(x)
  return y

my_list = [10, 45, 67, 23, 1, 87, 34, 99, 56, 33, 72, 91, 2, 10, 45, 23, 1, 45, 87, 56]
my_set = listToSet(my_list)
print(my_set)