def main():
    print_messages()

def print_messages():
    total_points = 0
    print_initial_message()

    response = input('1. I feel that I am a person of worth, at least on an equal plane with others. ')
    point_by_response = points_by_response(response, False)
    total_points += point_by_response

    response = input('2. I feel that I have a number of good qualities. ')
    point_by_response = points_by_response(response, False)
    total_points += point_by_response

    response = input('3. All in all, I am inclined to feel that I am a failure ')
    point_by_response = points_by_response(response, True)
    total_points += point_by_response

    response = input('4. I am able to do things as well as most other people. ')
    point_by_response = points_by_response(response, False)
    total_points += point_by_response

    response = input('5. I feel I do not have much to be proud of. ')
    point_by_response = points_by_response(response, True)
    total_points += point_by_response    

    response = input('6. I take a positive attitude toward myself. ')
    point_by_response = points_by_response(response, False)
    total_points += point_by_response
    
    response = input('7. On the whole, I am satisfied with myself. ')
    point_by_response = points_by_response(response, False)
    total_points += point_by_response

    response = input('8. I wish I could have more respect for myself. ')
    point_by_response = points_by_response(response, True)
    total_points += point_by_response

    response = input('9. I certainly feel useless at times. ')
    point_by_response = points_by_response(response, True)
    total_points += point_by_response

    response = input('10. At times I think I am no good at all. ')
    point_by_response = points_by_response(response, True)
    total_points += point_by_response                

    print_final_message( total_points )
def points_by_response(response, inverse):
    points = 0
    if not inverse:
         if response == 'D':
             points = 0
         elif response == 'd':
             points = 1

         elif response == 'a':
             points = 2
         elif response == 'A':
            points = 3
    else :
        if response == 'D':
             points = 3
        elif response == 'd':
             points = 2

        elif response == 'a':
             points = 1
        elif response == 'A':
            points = 0
    return points

def print_final_message(total_score):
    print(f'Your score is { total_score }')
    print('A score below 15 may indicate problematic low self-esteem.')

    if total_score < 15:
        print('You have a problematic low self-esteem :/ .')

def print_initial_message():
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    print()
main()