import csv
from datetime import datetime
from time import time


def main():
    INDEX_ITEM_ID = 0
    try:
        products_dict = read_dict('products.csv', INDEX_ITEM_ID)
        #print(f'Products {products_dict}')
        items_price = []
        items_number = 0
        subtotal = 0
        sales_tax = 0.06
        sales_tax_amount = 0
        total = 0
        with open('request.csv', 'rt') as request_csv:
            PRODUCT_INDEX = 0
            NUMBER_OF_PRODUCTS = 1
            reader = csv.reader(request_csv)
            next(reader)
            print('Requested Items')
            print()
            for row in reader:
                product_id = row[PRODUCT_INDEX]
                quantity_product = int(row[NUMBER_OF_PRODUCTS])

                # sum the numbers of items that the user wants to buy
                items_number += quantity_product

                # find the product in the dictionary by the id of the products
                dictionary_product = products_dict[product_id]
                
                [id, name, price] = dictionary_product
                price = float(price)
                # adding each total peer item [ 5$ * 4 ]
                items_price.append(price * quantity_product)
                print(f'{name}: {quantity_product} @ {price}')

            subtotal = round(sum(items_price), 2)
            sales_tax_amount = round(subtotal * sales_tax, 2)
            total = subtotal + sales_tax_amount
            print_final_message(items_number, subtotal,
                                sales_tax_amount, total)

    except (FileNotFoundError, PermissionError) as err:
        print('file not found or you have not permission to watch it')
        print(err)
    except KeyError as err:
        print('Error: unknown product ID in the request.csv file')
        print(err)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    with open(filename, 'rt') as csv_flle:
        dictionary = {}
        reader = csv.reader(csv_flle)
        next(reader)
        for row in reader:
            key_value = row[key_column_index]
            dictionary[key_value] = row
    return dictionary


def print_final_message(n_items, sub, sal_tax, total):
    """ print the bottom of the recip

    Parameters:
        n_items: Total number of items
        sub: subtotal price
        sal_tax: sales taxes amount
        total: total of all the prices

     """
    print()
    print('Thanks for bought here!')
    print('##############################################')
    print(f'Number of Items: {n_items}')
    print(f'Subtotal: {sub}')
    print(f'Sales Tax: {sal_tax}')
    print(f'Total: {total}')
    print('Thank you for shopping at the Inkom Emporium.')
    current_date_and_time = datetime.now(tz=None)
    #print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
    print(f'{current_date_and_time:%c}')
    print('##############################################')


if __name__ == '__main__':
    main()
