# seed.py
from reports.models import Store, Product, Sale
import random

print("Seeding database...")
Store.objects.all().delete()

store_names = ["MegaMart", "SuperStore", "BudgetBuy", "CornerShop", "The Mall"]
product_names = ["Apple", "Banana", "Orange", "Bread", "Milk", "Cheese", "Chicken", "Beef", "Soda", "Chips"]

for store_name in store_names:
    store = Store.objects.create(name=store_name)
    for prod_name in product_names:
        product = Product.objects.create(
            store=store,
            name=f"{prod_name} ({store_name[0]})",
            price=random.uniform(1.0, 10.0)
        )
        
        for _ in range(random.randint(5, 50)): # Create 5-50 sales per product
            Sale.objects.create(product=product, quantity=random.randint(1, 5))

print(f"Database seeded with {Store.objects.count()} stores.")
print(f"Total products: {Product.objects.count()}")
print(f"Total sales: {Sale.objects.count()}")