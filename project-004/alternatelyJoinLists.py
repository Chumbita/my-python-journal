def alternatelyJoinLists(list1, list2):
  i = 0
  j = 0
  new_list = list(set())
  while i < len(list1) or j < len(list2):
    if(i < len(list1)):
      new_list.append(list1[i])
      i += 1
    if (j < len(list2)):
      new_list.append(list2[j])
      j += 1

  return new_list
    
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 11, 23]

list3 = alternatelyJoinLists(list1, list2)
print(list3)
    