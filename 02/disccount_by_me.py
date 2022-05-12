from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
# Print the day of the week for the user to see.
print(day_of_week)

subtotal = 0
total = 0
disccount = 0
discount_amount = 0
taxes = 0.06
subtotal = float( input('what is the subtotal amount? ') )
if day_of_week == 2 or day_of_week == 3 and subtotal >= 50 :
        #apliying dsccount
    discount_amount = subtotal * 0.1
    subtotal = subtotal * 0.9
    taxes = subtotal * taxes
    total = subtotal + taxes
    print(f'Discount amount: {discount_amount:.2f}')
else :
    taxes = subtotal * taxes
    total = subtotal + taxes

print(f'Sales tax amount: {taxes}')
print(f'Total: { total }')


