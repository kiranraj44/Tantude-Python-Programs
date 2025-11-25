def aggregate_product_sales(sales_data, target_product):
    total_sales = 0
    breakdown = []
    for region in sales_data:
        sales = sales_data[region].get(target_product, 0)
        total_sales += sales
        if sales > 0:
            breakdown.append(str(sales))
    if breakdown:
        print(f"{target_product} total sales = {total_sales} ({' + '.join(breakdown)})")
    else:
        print(f"{target_product} total sales = 0 (no sales found)")

sales_data = {
    "North": {"Laptop": 1200, "Mouse": 50, "Keyboard": 75},
    "South": {"Laptop": 1500, "Monitor": 300, "Mouse": 60},
    "East": {"Keyboard": 80, "Monitor": 250},
    "West": {"Laptop": 1000, "Mouse": 45}}

a=input("Enter the target product: ")
aggregate_product_sales(sales_data,a)
b=input("Enter the targert product: ")
aggregate_product_sales(sales_data,b)
c=input("Enter the targert product: ")
aggregate_product_sales(sales_data,c)
  
