def main():
    number_repeated = 0
    list = read_file('provinces.txt')
    list.pop(0)
    list.pop()
    print(list)
    print()

    for index in range( len( list ) ):        
        if list[index] == 'AB':
            list[index] = 'Alberta'

    number_repeated = list.count('Alberta')
    print(f'The number of times that Alberta is present is {number_repeated}')
"""     for province in corrected_list:
        print(province) """

def read_file(filename):
    corrected_list = []
    with open(filename, 'rt') as file_text:
        for row in file_text:
            row = row.strip()
            corrected_list.append(row)
    return corrected_list
main()