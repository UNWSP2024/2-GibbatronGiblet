def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    item_price_1 = float(input("Enter item price 1: "))
    item_price_2 = float(input("Enter item price 2: "))
    item_price_3 = float(input("Enter item price 3: "))
    item_price_4 = float(input("Enter item price 4: "))
    item_price_5 = float(input("Enter item price 5: "))
    # then displays the subtotal of the sale,
    subtotal = item_price_1 + item_price_2 + item_price_3 + item_price_4 + item_price_5
    # the amount of sales tax, and the total.
    sales_tax = 0.07 * subtotal
    total = subtotal + sales_tax
    # Assume the sales tax is 7 percent.
    print ("Subtotal:", subtotal)
    print ("Sales tax:", sales_tax)
    print ("Total:", total)
calculate_total_purchase()
# Written by Logan Gibson on 9/9/25
# This program is titled "Digital Receipt"
