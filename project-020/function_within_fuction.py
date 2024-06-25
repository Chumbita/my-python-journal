def duplicate(num):
  return num * 2

def mydef(func, arr):
  arr_output = []
  for i in range(len(arr) - 1):
    arr_output.append(func(arr[i]))
  return arr_output

numbers = [1,2,3,4,5,6,7,8,9]
mylist = mydef(duplicate, numbers)
print(f'{numbers}\n{mylist}')