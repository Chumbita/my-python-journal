from Producto import Producto
class Inventario:
  def __init__(self):
    self.products = []

  def listar_productos(self):
    print(f"{"Name":<15}{"Price":<8}{"Category":<20}")
    for product in self.products:
      print(f"{product.name:<15}{product.price:<8}{product.category:<20}")
      
  def filter_products(self, category, min_price, max_price):
    products = filter(lambda p: p.category == category and p.price >= min_price and p.price <= max_price, self.products)
    return products

  def apply_discount(self, category, min_price, max_price, discount):
    products_without_discount = self.filter_products(category, min_price, max_price)
    products_with_discount = map(lambda p: p.price - p.rice * (discount / 100), products_without_discount)
  
