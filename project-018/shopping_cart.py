def aplicar_descuento(precio, porcentaje):
  return precio - precio * porcentaje

def aplicar_IVA(precio, porcentaje):
  return precio * (porcentaje + 1)

def calculo_precio_final(carrito):
  sub_total = 0
  total = 0
  print(f"{'Producto':<15} {'Precio':<10} {'Descuento':<10} {'Total':<10}\n{'-' * 45}")
  # print(f"{'Producto':<15} {'Precio':<10} {'IVA':<10} {'Total':<10}\n{'-' * 45}")
  for x in carrito.keys():
    sub_total = aplicar_descuento(carrito[x][0], carrito[x][1])
    total += aplicar_descuento(carrito[x][0], carrito[x][1])
    # sub_total = aplicar_IVA(carrito[x][0], carrito[x][1])
    # total += aplicar_IVA(carrito[x][0], carrito[x][1])
    print(f"{x:<15} ${carrito[x][0]:<9.2f} {carrito[x][1]:<9.2f} {sub_total:<10.2f}")
  
  print(f"\nTotal {'-' * 30} ${total:.2f}")

carrito = {
    "manzanas": [1.20, 0.10],
    "pan": [1.50, 0.05],
    "leche": [0.99, 0.12],
    "huevos": [2.00, 0.08],
    "pollo": [5.99, 0.15],
    "arroz": [1.30, 0.07],
    "pasta": [1.10, 0.10],
    "queso": [3.50, 0.05],
    "tomates": [2.20, 0.10],
    "jugo": [1.75, 0.12]
}

calculo_precio_final(carrito)