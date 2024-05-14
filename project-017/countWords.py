def wordCounter(string):
  words_array = string.split(" ")
  words_dict = dict()

  for word in words_array:
    occurs = string.count(word)
    words_dict[word] = occurs

  return words_dict

def theMostRepeatedWord(dictionary):
  word = ""
  ocurrs = 0

  for key in dictionary.keys():
    if dictionary[key] > ocurrs:
      word = key
      ocurrs = dictionary[key]

  return tuple((word, ocurrs))

sentence = "Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."

var1 = wordCounter(sentence)
var2 = theMostRepeatedWord(var1)
print(var1)
print(var2)