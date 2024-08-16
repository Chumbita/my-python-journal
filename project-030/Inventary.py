from Product import Products
class Inventary:
  def __init__(self):
    self.products = []

  def list_products(self):
    print(f"{'Name':<15}{'Price':<8}{'Category':<20}")
    for product in self.products:
      print(f"{product.name:<15}{product.price:<8}{product.category:<20}")
      
  def filter_products(self, category, min_price, max_price):
    products = filter(lambda p: p.category == category and p.price >= min_price and p.price <= max_price, self.products)
    return list(products)

  def apply_discount(self, products, discount):
    list(map(lambda p: setattr(p, 'price', p.price - p.price * (discount / 100)), products))
    return products