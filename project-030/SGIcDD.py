'''Sistema de Gestión de Inventario con Descuentos Dinámicos'''
from Product import Product
from Inventary import Inventary
import os

mi_inventary = Inventary()
my_products = [
Product("Butter", 2.50, "Dairy"),
Product("Milk", 1.20, "Dairy"),
Product("Cheese", 3.00, "Dairy"),
Product("Yogurt", 0.90, "Dairy"),
Product("Bread", 1.50, "Bakery"),
Product("Croissant", 2.00, "Bakery"),
Product("Muffin", 1.80, "Bakery"),
Product("Bagel", 1.70, "Bakery"),
Product("Juice", 2.00, "Beverages"),
Product("Soda", 1.50, "Beverages"),
Product("Water", 0.80, "Beverages"),
Product("Coffee", 3.00, "Beverages"),
Product("Chips", 1.30, "Snacks"),
Product("Cookies", 2.50, "Snacks"),
Product("Candy", 1.00, "Snacks"),
Product("Chocolate", 1.80, "Snacks"),
Product("Apple", 0.50, "Produce"),
Product("Banana", 0.30, "Produce"),
Product("Carrot", 0.20, "Produce"),
Product("Lettuce", 0.70, "Produce")]

mi_inventary.products = my_products

def main():
  flag = True
  while flag:
    os.system('cls')
    print('-----|Inventory Management System with Dynamic Discounts|-----\n1)List Products.\n2)Apply Filter.\n3)Apply Discount.\n4)Exist.')
    user_choice = int(input("Choose an operation: "))
    os.system('cls')
    if user_choice == 1:
      mi_inventary.listar_productos()
    elif user_choice == 2:
      print("-----|APPLY FILTER|-----\nIMPORTANT: The filter is applied by category and by a price range\n")
      category = input("Enter the category: ")
      min_price = float(input("Enter the min price: $"))
      max_price = float(input("Enter the max price: $"))
      os.system('cls')
      print(f"-----|APPLY FILTER|-----\n-Filter: {category}\n-Min-Price: ${min_price}\n-Max-Price: ${max_price}\n\nProducts:")
      products = mi_inventary.filter_products(category, min_price, max_price)
      for p in products:
        print(f"-{p.name} ${p.price} [{p.category.upper()}].")
    elif user_choice == 3: 
      print("-----|APPLY DISCOUNT|-----\nIMPORTANT: The discount is applied by category, by a price range and you must enter the discount percentage without the '%'\n")
      category = input("Enter the category ")
      min_price = float(input("Enter the min price: $"))
      max_price = float(input("Enter the max price: $"))
      discount = float(input("Enter the dicount: "))
      os.system('cls')
      print(f"-----|APPLY DISCOUNT|-----\n-Filter: {category}\n-Min-Price: ${min_price}\n-Max-Price: ${max_price}\n-Discount: {discount}%.\n\nProducts:")
      non_discounted_products = mi_inventary.filter_products(category, min_price, max_price)
      discounted_products = mi_inventary.apply_discount(non_discounted_products, discount)
      for p in discounted_products:
        print(f"{p.name} ${p.price} {p.category.upper()}.")
    elif user_choice == 4:
      flag = not flag
    else:
      print("Invalid option")
    input("Press ENTER to continue...")

if __name__ == '__main__':
  main()