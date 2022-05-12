from datetime import datetime
import math


current_date_and_time = datetime.now()

#Print only the date part of the current date and time.
#print(f"{current_date_and_time:%Y-%m-%d}")

width_tire = 0
aspect_ratio_tire = 0
diameter_tire = 0
π = math.pi
volume_tire = 0
user_answer = 'no'

with open('volumes.txt', 'at') as volumes_file:
    while user_answer == 'no':
        if width_tire != 0 :
            # I check if it different than 0 to not save the first time values
            print(f'previous data not chosen: {current_date_and_time:%Y-%m-%d}, {width_tire}, {aspect_ratio_tire}, {diameter_tire}, {volume_tire} ', file=volumes_file)
        #inputs
        width_tire = int( input('[W] Enter the width of the tire in mm (ex 205): '))
        aspect_ratio_tire = int( input('[a] Enter the aspect ratio of the tire (ex 60): ') )
        diameter_tire = int( input('[d] Enter the diameter of the wheel in inches (ex 15): '))
        volume_tire = ( π * (width_tire ** 2) * aspect_ratio_tire * ( width_tire * aspect_ratio_tire + 2540 * diameter_tire ) ) / 10000000000
        #end inputs
        print(f'The approximate volume is { volume_tire:0.2f} liters')
        print('#############################################################')
        user_answer = input('Do you want to buy a tier with those properties? yes/no: ')
        user_answer = user_answer.lower()

    #writting in the tex file
    print(f'Tier bought: {current_date_and_time:%Y-%m-%d}, {width_tire}, {aspect_ratio_tire}, {diameter_tire}, {volume_tire} ', file=volumes_file)
"""     print(f'{width_tire}', file=volumes_file)
    print(f'{aspect_ratio_tire}', file=volumes_file)
    print(f'{diameter_tire}', file=volumes_file)
 """
    