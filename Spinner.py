# -----------------------------------------------------------------------------

#

# Fidget Spinner Simulation

# Language - Python

# Modules - pygame, sys, math

#

# Controls : Left and Right arrows to rotate the Spinner in direction, spacebar to change color of Spinner

#            the Longer you press arrow key the more speed it reaches!

#

# By - Jatin Kumar Mandav

#

# Website - https://jatinmandav.wordpress.com

#

# YouTube Channel - https://www.youtube.com/channel/UCdpf6Lz3V357cIZomPwjuFQ

# Facebook - https://www.facebook.com/jatinmandav

# Twitter - @jatinmandav

# Email - jatinmandav3@gmail.com

#

# -----------------------------------------------------------------------------

'''
Comments by Alejandro Meza
Date: 17/07/2020
'''

import pygame #first module to import

#Sys-module provides access to some variables used or maintained by the interpreter and to functions that interact
#strongly with the interpreter. It is always available
import sys

from math import * #So we import all the stuff in order to
#achieve a high performance

# Initialization of Pygame Window

#With pygame.init we initialize all the imported modules
pygame.init()

#the width of our window gonna have this measure
#500 is a good measure to start our visual representation
width = 500
#the height of our window gonna have this measure
height = 500

display = pygame.display.set_mode((width, height))

#Now we are gonna see some stuff about time
#Firs of all, we are capable of obtaint the time in msg with
#the method pygame.time.get_tickets()  --> return 0 if is used before init()
#With the following line, we create a clock
clock = pygame.time.Clock()

#This is gonna be the label of the window
pygame.display.set_caption("Our Fidget Spinner Simulation")


# Colors --> (red, green, blue)
#Colors in Python are expressed according how much red, green
#and blue do they have in them ... --> RGB pattern

background = (51, 51, 51)

white = (240, 240, 240)

red = (176, 58, 46)

dark_red = (120, 40, 31)

dark_gray = (23, 32, 42)

blue = (40, 116, 166)

dark_blue = (26, 82, 118)

yellow = (183, 149, 11)

dark_yellow = (125, 102, 8)

green = (29, 131, 72)

dark_green = (20, 90, 50)

orange = (230, 126, 34)

dark_orange = (126, 81, 9)


# Close the Pygame Window

def close():
    pygame.quit()

    sys.exit()


# Drawing of Fidget Spinner on Pygame Window

def show_spinner(angle, color, dark_color):
    d = 80

    innerd = 50

    x = width / 2 - d / 2

    y = height / 2

    l = 200

    r = l / (3 ** 0.5)

    w = 10

    lw = 60

    # A little math for calculation the coordinates after rotation by some 'angle'

    # x = originx + r*cos(angle)

    # y = originy + r*sin(angle)

    centre = [x, y, d, d]

    centre_inner = [x + d / 2 - innerd / 2, y + d / 2 - innerd / 2, innerd, innerd]

    top = [x, y - l / (3) ** 0.5, d, d]

    top_inner = [x, y - l / (3) ** 0.5, innerd, innerd]

    top[0] = x + r * cos(radians(angle))

    top[1] = y + r * sin(radians(angle))

    top_inner[0] = x + d / 2 - innerd / 2 + r * cos(radians(angle))

    top_inner[1] = y + d / 2 - innerd / 2 + r * sin(radians(angle))

    left = [x - l / 2, y + l / (2 * (3) ** 0.5), d, d]

    left_inner = [x, y - l / (3) ** 0.5, innerd, innerd]

    left[0] = x + r * cos(radians(angle - 120))

    left[1] = y + r * sin(radians(angle - 120))

    left_inner[0] = x + d / 2 - innerd / 2 + r * cos(radians(angle - 120))

    left_inner[1] = y + d / 2 - innerd / 2 + r * sin(radians(angle - 120))

    right = [x + l / 2, y + l / (2 * (3) ** 0.5), d, d]

    right_inner = [x, y - l / (3) ** 0.5, innerd, innerd]

    right[0] = x + r * cos(radians(angle + 120))

    right[1] = y + r * sin(radians(angle + 120))

    right_inner[0] = x + d / 2 - innerd / 2 + r * cos(radians(angle + 120))

    right_inner[1] = y + d / 2 - innerd / 2 + r * sin(radians(angle + 120))

    # Drawing shapes on Pygame Window

    #with .line we are able to draw a kind of rectangle
    #with .ellipse we are able to draw a kind of circle
    pygame.draw.line(display, dark_color, (top[0] + d / 2, top[1] + d / 2), (centre[0] + d / 2, centre[1] + d / 2), lw)

    pygame.draw.line(display, dark_color, (left[0] + d / 2, left[1] + d / 2), (centre[0] + d / 2, centre[1] + d / 2),
                     lw)

    pygame.draw.line(display, dark_color, (right[0] + d / 2, right[1] + d / 2), (centre[0] + d / 2, centre[1] + d / 2),
                     lw)
    #centre circle
    pygame.draw.ellipse(display, color, tuple(centre))
    #centre inner circle
    pygame.draw.ellipse(display, dark_color, tuple(centre_inner))

    #top circle
    pygame.draw.ellipse(display, color, tuple(top))
    #top inner circle
    pygame.draw.ellipse(display, dark_gray, tuple(top_inner), 10)

    #left circle
    pygame.draw.ellipse(display, color, tuple(left))
    # left inner circle
    pygame.draw.ellipse(display, dark_gray, tuple(left_inner), 10)

    #right circle
    pygame.draw.ellipse(display, color, tuple(right))
    #right inner circle
    pygame.draw.ellipse(display, dark_gray, tuple(right_inner), 10)


# Displaying Information on Pygame Window

def show_info(friction, speed):
    #Define the font of the window that we are gonna use
    font = pygame.font.SysFont("Times New Roman", 18)

    frictionText = font.render("Friction : " + str(friction), True, green)
    colorText = font.render("Tap space to change the color ", True, green)
    speedText = font.render("Rate of Change of Angle : " + str(speed), True, green)

    #uptade alll the time the data
    #in order to achieve this --> 'overfdraw text'
    display.blit(speedText, (15, 15))
    display.blit(frictionText, (15, 45))
    display.blit(colorText, (15, 75))


# The Main Function

def spinner():
    spin = True

    angle = 0

    speed = 0.0

    friction = 0.03 #initial value

    #when are ready to play, the spinner movement didnt exist
    rightPressed = False

    leftPressed = False

    direction = 1

    color = [[red, dark_red], [blue, dark_blue], [yellow, dark_yellow], [green, dark_green], [orange, dark_orange]]

    index = 0

    while spin:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_RIGHT:
                    rightPressed = True

                    direction = 1

                if event.key == pygame.K_LEFT:
                    leftPressed = True

                    direction = -1
                #If this happen, the color will change
                if event.key == pygame.K_SPACE:

                    index += 1

                    if index >= len(color):
                        index = 0

            if event.type == pygame.KEYUP:
                leftPressed = False

                rightPressed = False

        # Changing the Angle of rotation

        if direction == 1:

            if rightPressed:

                speed += 0.3

            else:

                speed -= friction

                if speed < 0:
                    speed = 0.0

        else:

            if leftPressed:

                speed -= 0.3

            else:

                speed += friction

                if speed > 0:
                    speed = 0.0

        display.fill(background) #background is a color that we have defined

        angle += speed

        # Displaying Information and the Fidget Spinner

        show_spinner(angle, color[index][0], color[index][1])

        show_info(friction, speed)

        pygame.display.update()

        clock.tick(90) #for every second at most 90 frames should pass


spinner()