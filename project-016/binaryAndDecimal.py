def toBinary(decimal):
  n = decimal
  binary = ""
  while decimal > 0:
    binary += str(decimal % 2)
    decimal //= 2
  binary = binary[::-1]

  print(f"Decimal: {n}\nBinary: {binary}")

def toDecimal(binary):
  n = binary
  binary = str(binary)
  binary = binary[::-1]
  print(binary)
  decimal = 0
  for i in range(len(binary)):
    decimal += int(binary[i]) * 2**i

  print(f"Binary: {n}\nDecimal: {decimal}")

toBinary(22)
toDecimal(10110)

# Slicing [::-1] -> Sintaxis [inicio:fin:paso]
# Con esto estamos diciendo al programa que tome todos los elementos desde el principio hasta el final, pero en orden inverso.
