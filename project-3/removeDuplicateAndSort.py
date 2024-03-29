def removeDuplicates(list):
  new_list = []
  for x in list:
    if x not in new_list: 
      new_list.append(x)
  
  list.clear()
  list.extend(new_list)
  list.sort()

fruits = ['manzana', 'pera', 'uva', 'banana', 'naranja', 'kiwi', 'sandía', 'durazno', 'mandarina', 'melón', 'frutilla', 'limón', 'manzana', 'uva', 'pera', 'manzana', 'banana', 'uva', 'kiwi', 'naranja']

numbers = [10, 45, 67, 23, 1, 87, 34, 99, 56, 33, 72, 91, 2, 10, 45, 23, 1, 45, 87, 56]

print(f"-Fruits List Before: {fruits}")
removeDuplicates(fruits)
print(f"-Fruits List After: {fruits}")