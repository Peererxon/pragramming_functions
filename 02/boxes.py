""" 
Enter the number of items: 8
Enter the number of items per box: 5

For 8 items, packing 5 items in each box, you will need 2 boxes.
 """

import math


items = int( input( 'Enter the number of items: ' ) )
items_per_box = int( input('Enter the number of items per box: ') )
boxes_needed = math.ceil( items / items_per_box )
print()

print(f'For {items} items, packing {items_per_box} items in each box, you will need { boxes_needed } boxes.')