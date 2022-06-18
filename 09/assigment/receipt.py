import csv


def main():
    products_dict = read_dict('products.csv',0)
    print(f'Products {products_dict}')

    with open( 'request.csv', 'rt' ) as request_csv:
        PRODUCT_INDEX = 0
        NUMBER_OF_PRODUCTS = 1
        reader = csv.reader(request_csv)
        next(reader)
        print('Requested Items')
        print()
        for row in reader:
            product_id = row[PRODUCT_INDEX]
            quantity_product = int(row[NUMBER_OF_PRODUCTS])
            #find the product in the dictionary by the id of the products
            dictionary_product = products_dict[product_id]
            [ id,name,price ] = dictionary_product
            print(f'{name}: {quantity_product} @ {price}')
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
if __name__ == '__main__':
    main()