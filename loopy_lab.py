import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    # loop inside the first quadrant, leaving space between each block
    for row in range(5, 301, 10):
        for column in range(5, 301, 10):
            x = column
            y = row
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # loop through 30 rows and columns
    for row in range(30):
        for column in range(30):
            # determine what colour the columns should be
            if column % 2 != 0:
                colour = arcade.color.BLACK
            else:
               colour = arcade.color.WHITE
            # update pos variables and draw squares
            x = column*10 + 305
            y = row*10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, colour)


def draw_section_3():
    # loop through 30 columns and rows
    for row in range(30):
        for column in range(30):
            # determine what colour the row should be
            if row % 2 == 0:
                colour = arcade.color.WHITE
            else:
                colour = arcade.color.BLACK
            # update pos variables and draw squares
            x = column*10 + 605
            y = row*10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, colour)


def draw_section_4():
    # loop through to create multiple squares
    for row in range(30):
        for column in range(30):
            # set initial colour
            colour = arcade.color.WHITE

            # check if the block should be a different colour
            if row % 2 != 0 or column % 2 != 0:
                colour = arcade.color.BLACK

            # update x and y coordinates
            x = column*10 + 905
            y = row*10 + 5

            # draw a square
            arcade.draw_rectangle_filled(x, y, 5, 5, colour)



def draw_section_5():
    # make left triangle
    for row in range(30):
        for column in range(295, row*10, -10):
            # change x and y position of the cubes to be in the right quadrant
            x = column
            y = row*10 + 295

            # draw each square
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_6():
    # make right triangle
    for row in range(30):
        for column in range(305, ((30-row)*10) + 305, 10):
            # change x and y positions
            x = column
            y = row*10 + 305

            # draw each square
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    # make reflected right triangle left
    for row in range(1, 31):
        for column in range(605, (row*10) + 605, 10):
            # update the x and y pos
            x = column
            y = row*10 + 295

            # draw each square
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    # make reflected right triangle right
    for row in range(1, 31):
        # Do (-5+905) to account for the first bottom row
        for column in range(1195, ((30-row)*10) - 5 + 905, -10):
            # update the x and y pos
            x = column
            y = row*10 + 295

            # draw each square
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

# call the main function
main()