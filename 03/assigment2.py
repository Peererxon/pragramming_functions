# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import math
import random
from turtle import color, width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    
    draw_clouds( canvas, 50, 350, 250, 480 )
    draw_clouds( canvas, 50, 350, 250, 480 )

    draw_clouds( canvas, 380, 350, 500, 480 )
    draw_clouds( canvas, 380, 350, 500, 480 )

    draw_sun(canvas, scene_width, 80)

def draw_clouds( canvas, min_x, min_y, max_x, max_y ):
    cloud_width = 50
    cloud_height = 25
    initial_x = random.randint( min_x, max_x )
    initial_y = random.randint( min_y, max_y )
    draw_oval( canvas, initial_x, initial_y, initial_x + cloud_width, initial_y + cloud_height )
    for x in range( initial_x, initial_x + 200, cloud_width - 25  ):
        draw_oval( canvas, x, initial_y, x + cloud_width, initial_y + cloud_height, fill='cadetBlue1' )

    for x in range( initial_x, initial_x + 200, cloud_width - 25  ):
        draw_oval( canvas, x, initial_y + 5, x + cloud_width, initial_y + 5 + cloud_height, fill='cadetBlue1' )


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    peak_y_ground = scene_height / 3
    draw_rectangle(canvas, 0, 0,
        scene_width, peak_y_ground, width=0, fill="tan4")

    draw_grass(canvas, scene_width, peak_y_ground )
    draw_trees(canvas, scene_width, peak_y_ground )

    house_width = 200
    house_height = 250
    x_house = random.randint(house_width, scene_width - house_width)
    draw_house( canvas, x_house, peak_y_ground , house_width,house_height, color='darkSalmon'  )

def draw_grass( canvas, scene_width,max_top, ):
    for x in range(1600):
        random_x = random.randint( 3, scene_width - 3 )
        
        random_y = random.randint( 0, math.ceil(max_top) )
        draw_rectangle( canvas, random_x, random_y, random_x + 3, random_y + 30, fill='forestGreen', width=0.1 )

def draw_trees( canvas, scene_width, max_top):
    """ Draw tres inside of the limit of the scene with random values """
    for x in range( 20 ):
        tree_height = random.randint( 80, 150 )
        tree_center_x = random.randint(0 + math.ceil( tree_height / 10 ) , scene_width - math.ceil( tree_height / 10 ) )
        tree_bottom = random.randint( 0, math.ceil(max_top) )
        draw_pine_tree(canvas, tree_center_x,
                tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_sun( canvas, center_x, diameter, initial_y= 150 ):
    peak_y = initial_y + diameter
    left_x = (center_x / 2) - diameter
    draw_oval(canvas, left_x, initial_y - diameter, (center_x / 2) + diameter, peak_y, fill="yellow1")
    #draw_line( canvas, left_x, initial_y, left_x, initial_y + 40, fill='green'  )
    draw_sun_details( canvas, center_x / 2, peak_y )
    """ draw_oval( canvas, center_x, height,  ) """

def draw_sun_details( canvas,center_x, peak_y ):
    """ print the sun rays around the sun """
    difference_right = 8
    difference_left = 20
    light_height = 35
    #center
    draw_line( canvas, center_x, peak_y, center_x, peak_y + light_height, fill='yellow1', width=2  )

    draw_sun_details_rigth( canvas, center_x, difference_right, peak_y, difference_left, light_height )

    draw_sun_details_left(canvas, center_x, difference_right, peak_y, difference_left, light_height)

def draw_sun_details_left ( canvas,center_x, displacement_right, peak_y, displacement_left, light_height  ):
    """ left side """
    draw_line( canvas, center_x - displacement_right, peak_y - displacement_right, center_x - displacement_left, peak_y + light_height, fill='yellow1', width=2  )
    draw_line( canvas, center_x - displacement_right * 2, peak_y - displacement_right *2, center_x - displacement_left * 2, peak_y + light_height * 0.7, fill='yellow1', width=2  )
    draw_line( canvas, center_x - displacement_right * 2.8, peak_y - displacement_right * 2.8, center_x - displacement_left * 2.8, peak_y + light_height * 0.4, fill='yellow1', width=2  )
    draw_line( canvas, center_x - displacement_right * 3.5, peak_y - displacement_right * 3.5, center_x - displacement_left * 3.5, peak_y + light_height * 0.02, fill='yellow1', width=2  )

def draw_sun_details_rigth ( canvas, center_x, displacement_right, peak_y, displacement_left, light_height ):
    """ Right side """
    draw_line( canvas, center_x + displacement_right, peak_y - displacement_right, center_x + displacement_left, peak_y + light_height, fill='yellow1', width=2  )
    draw_line( canvas, center_x + displacement_right * 2, peak_y - displacement_right *2, center_x + displacement_left * 2, peak_y + light_height * 0.7, fill='yellow1', width=2  )
    draw_line( canvas, center_x + displacement_right * 2.8, peak_y - displacement_right * 2.8, center_x + displacement_left * 2.8, peak_y + light_height * 0.4, fill='yellow1', width=2  )
    draw_line( canvas, center_x + displacement_right * 3.5, peak_y - displacement_right * 3.5, center_x + displacement_left * 3.5, peak_y + light_height * 0.02, fill='yellow1', width=2  )

def draw_house( canvas, center_x, center_y, width_house, height_house, color ):
    draw_bottom_house( canvas, center_x, center_y, width_house, height_house, color )

    draw_top_house( canvas, center_x, center_y, width_house, height_house, color )
    
    draw_door( canvas, center_x, center_y, width_house / 3.5, height_house / 2.2 )

def draw_bottom_house( canvas, center_x, bottom_house, house_width, house_height, color ):
    """ draw the first half bottom of the house """
    halft_house_width = house_width / 2
    bottom_left_house = center_x - halft_house_width
    half_house_height = house_height / 2
    draw_rectangle( canvas, bottom_left_house, bottom_house, 
        center_x + halft_house_width, bottom_house + half_house_height, 
        fill=color
    )

def draw_top_house( canvas, center_x, center_y, house_width, house_height, color):
    """ Draw the top of the house """
    """ I need:
        leftside
        middlePoint
        rigthSide
     """
    left_side = center_x - house_width / 2
    bottom_first_half = center_y + ( house_height / 2 )  #this is the peak_y of the bottom halft of the house
    top_house =  center_y + house_height
    right_side = center_x + house_width / 2
    draw_polygon( canvas, left_side, bottom_first_half, center_x , top_house , right_side , bottom_first_half, fill=color )

    """ draw a circle in the middle of the top house """
    window_width = 15
    half_top_house = (bottom_first_half + top_house) / 2
    draw_oval( canvas, center_x - window_width, half_top_house - window_width , center_x + window_width, half_top_house + window_width, fill='gray85'  )

def draw_door( canvas, center_x, center_y, door_width, height_door ):
    #right_x_door = center_x + door_width
    center_y_door = center_y + (height_door / 2)
    halft_door_width = door_width / 2
    draw_rectangle( canvas, center_x - halft_door_width, center_y, center_x + halft_door_width, center_y + height_door, width=2, fill='orange' )
    draw_door_lock( canvas, center_x + halft_door_width, center_y_door )

def draw_door_lock( canvas, right_x_door, center_y ):
    """ draw the lock of the door in the center """
    draw_oval( canvas, right_x_door - 20, center_y, right_x_door - 5 , center_y + 15, fill='yellow')
# Call the main function so that
# this program will start executing.
main()