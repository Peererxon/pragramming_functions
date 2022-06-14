import csv


def read_dict(filename, key_column_index):
    KEY_COLUMN_VALUE = 1
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as csv_file:

        reader_csv = csv.reader(csv_file)
        next(reader_csv)
        for row in reader_csv:
            key = row[key_column_index]
            dictionary[ key ] = row[KEY_COLUMN_VALUE]
    return dictionary

def main():
    dictionary = read_dict('students.csv',0,)
    identifier = input('What I-Number do you want to search for? ')
    if identifier in dictionary:
        print(dictionary[identifier])
    else:
        print('No such student')
main()