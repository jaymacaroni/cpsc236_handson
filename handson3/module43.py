taxrate = 0.06 # constant

def calculate_sales_tax(subtotal):
    sales_tax = subtotal * taxrate
    return round(sales_tax, 2)

def calculate_total_after_tax(subtotal):
    sales_tax = calculate_sales_tax(subtotal)
    total_after_tax = subtotal + sales_tax
    return round(total_after_tax, 2)
