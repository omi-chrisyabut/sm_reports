# reports/tasks.py
from .models import Store, Product, Sale
from django.db import connection
import time

def generate_store_performance_report():
    """
    Generates a performance report for all stores.

    This function is VERY SLOW and needs to be optimized.
    """
    print("Running report...")
    start_time = time.time()

    connection.queries_log.clear()

    stores = Store.objects.all()

    report = []

    for store in stores:

        product_count = store.products.count()

        sales = Sale.objects.filter(product__store=store)

        total_revenue = 0
        for sale in sales:
            total_revenue += sale.quantity * sale.product.price

        best_product_name = "N/A"
        max_revenue = 0

        for product in store.products.all():
            product_revenue = 0

            for sale in product.sales.all():
                product_revenue += sale.quantity * product.price 

            if product_revenue > max_revenue:
                max_revenue = product_revenue
                best_product_name = product.name

        report.append({
            "store_name": store.name,
            "product_count": product_count,
            "total_revenue": total_revenue,
            "best_selling_product": best_product_name
        })

    end_time = time.time()
    print(f"Report finished in {end_time - start_time:.4f} seconds.")
    print(f"Total queries: {len(connection.queries)}")

    return report