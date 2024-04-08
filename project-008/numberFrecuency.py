def numberFrecuency(tuple):
  x = dict()
  for i in range(len(tuple)):
    if tuple[i] not in x.keys():
      x[tuple[i]] = tuple.count(tuple[i])

  return x

my_tuple = tuple((1, 2, 2, 3, 1, 4, 5, 4))

x = numberFrecuency(my_tuple)
print(x)