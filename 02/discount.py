""" 
 python discount.py
Please enter the subtotal: 42.75
Sales tax amount: 2.56
Total: 45.31

 """

from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

discount = 0
subtotal = float( input('Please enter the subtotal: ') )
sales_tax_amount = subtotal * ( 0.06 )
total = subtotal + sales_tax_amount

############
if day_of_week == 2 or day_of_week == 3 and subtotal >= 50:

    discount = subtotal * 0.10
    taxdiscount = (subtotal - discount) * 6 /100
    totaldiscount = subtotal - discount + taxdiscount
    print (f"Discount amount: {discount:.2f}")
    print (f"Sales tax amount: {taxdiscount:.2f}")
    print (f"Total: {totaldiscount:.2f}")
    print()
    
else:   
    print (f"Sales tax amount: {sales_tax_amount:.2f}")
    print (f"Total: {total:.2f}") 