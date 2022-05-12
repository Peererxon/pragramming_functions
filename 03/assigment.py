# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky( canvas, scene_height, scene_width )

    draw_ground( canvas, scene_height, scene_width )

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, height, width):
    sky_limit = height / 2
    draw_rectangle(canvas, 0, height, width, sky_limit,  fill='dodgerBlue1')

    cloud_width = 70
    cloud_height = 35
"""     space = 0
    for x in range( 0, width, 30 ):
        draw_oval( canvas, x, sky_limit, x + cloud_width, sky_limit + cloud_height, fill='orange' )
        space += 20 """

def draw_cloud( canvas, x_center,y_center, width, height ):
    draw_oval(canvas, x_center, y_center, width, height )
    print('i am a cloud my broh!')

def draw_ground( canvas, height, width ):
    top_ground = height / 4
    draw_rectangle( canvas, 0, 0, width, top_ground, fill='brown'  )
    draw_rocks(canvas, top_ground, width)

def draw_rocks( canvas, height, width ):
    rock_center = 80 / 2
    #draw_line(canvas, 0, 10 , line_width, 10, fill='black' )
    #pick of the line rock
    peak_rock_height = 80
    rock_width = 50
    triangle_angle = 20
    #draw_polygon( canvas, rock_center, 10, rock_center - 50, 10, rock_center - triangle_angle, peak_rock_height, fill='orange', width=1 )
    space = 20
    for x in range(10, width, 25):
        draw_polygon( canvas, x + space, 10, x + rock_width, 10, x + triangle_angle, peak_rock_height, fill='yellow', width=1 )
# Call the main function so that
# this program will start executing.
main()