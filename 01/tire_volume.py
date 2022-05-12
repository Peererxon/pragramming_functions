""" 
v =  π w2 aw a + 2,540 d
        10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24.09 liters

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15

The approximate volume is 39.92 liters

 """

import math


width_tire = int( input('[W] Enter the width of the tire in mm (ex 205): '))
aspect_ratio_tire = int( input('[a] Enter the aspect ratio of the tire (ex 60): ') )
diameter_tire = int( input('[d] Enter the diameter of the wheel in inches (ex 15): '))
π = math.pi
volume_tire = ( π * (width_tire ** 2) * aspect_ratio_tire * ( width_tire * aspect_ratio_tire + 2540 * diameter_tire ) ) / 10000000000

print(f'The approximate volume is { volume_tire:0.2f} liters')