""" 
Add code to reverse and print fruit_list.
Add code to append "orange" to the end of fruit_list and print the list.
Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
Add code to remove "banana" from fruit_list and print the list.
Add code to pop the last element from fruit_list and print the popped element and the list.
Add code to sort and print fruit_list.
Add code to clear and print fruit_list.
At the bottom of your program write a call to the main function.
 """


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print(fruit_list.reverse())

    print(fruit_list.append('orange'))

    apple_index = fruit_list.index('apple')
    fruit_list.insert(apple_index, 'cherry')
    print(f'after insert {fruit_list}')

    fruit_list.remove('banana')
    print(f'whiout banana {fruit_list}')

    fruit_list.pop()
    print(f'poped {fruit_list}')

    fruit_list.sort()
    print(fruit_list)

    fruit_list.clear()
    print(fruit_list)


main()
