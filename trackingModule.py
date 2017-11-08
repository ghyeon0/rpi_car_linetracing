#########################################################################
### Date: 2017/10/13
### file name: trackingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
###
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time
import getLine
import movement

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)


# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Raspberry Pi
# as the control pins of 5-way tracking sensor in order to
# control direction
# 
#  leftTwo    leftOne     center     rightOne     rightTwo
#       16            18              22             40              32
#
# led turns on (1) : tracking sensor led detects white playground
# led turns off(0) : tracking sensor led detects black line

# leftTwo off : it means that moving object finds black line
#                   at the position of leftTwo
#                   black line locates below the leftTwo of the moving object
#
# leftOne off : it means that moving object finds black line
#                   at the position of leftOne
#                   black line locates below the leftOne of the moving object
# 
# center off : it means that moving object finds black line
#                   at the position of center
#                   black line locates below the center of the moving object
# 
# rightOne off : it means that moving object finds black line
#                   at the position of rightOne
#                   black line locates below the rightOne  of the moving object
# 
# rightTwo off : it means that moving object finds black line
#                   at the position of rightTwo
#                   black line locates below the rightTwo of the moving object
# =======================================================================

leftTwo = 16
leftOne = 18
center = 22
rightOne = 40
rightTwo = 32


# =======================================================================
# because the connections between 5-way tracking sensor and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as leftTwo, leftOne, center, rightOne, and rightTwo
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftTwo, leftOne, center, rightOne, and rightTwo
# should be clearly declared as input
# 
# =======================================================================

GPIO.setup(leftTwo, GPIO.IN)
GPIO.setup(leftOne, GPIO.IN)
GPIO.setup(center,   GPIO.IN)
GPIO.setup(rightOne, GPIO.IN)
GPIO.setup(rightTwo, GPIO.IN)

# =======================================================================
# GPIO.input(leftTwo) method gives the data obtained from leftTwo
# leftTwo returns (1) : leftTwo detects white playground
# leftTwo returns (0) : leftTwo detects black line
#
#
# GPIO.input(leftOne) method gives the data obtained from leftOne
# leftOne returns (1) : leftOne detects white playground
# leftOne returns (0) : leftOne detects black line
#
# GPIO.input(center) method gives the data obtained from center
# center returns (1) : center detects white playground
# center returns (0) : center detects black line
#
# GPIO.input(rightOne) method gives the data obtained from rightOne
# rightOne returns (1) : rightOne detects white playground
# rightOne returns (0) : rightOne detects black line
#
# GPIO.input(rightTwo) method gives the data obtained from rightTwo
# rightTwo returns (1) : rightTwo detects white playground
# rightTwo returns (0) : rightTwo detects black line
#
# =======================================================================


try:
    while True:
        movement.pwm_setup()
        line_check = getLine.get_line()
        print(line_check)
        if line_check == ['0', '0', '0', '0', '0']:
            movement.stop()
        elif line_check == ['0', '1', '1', '1', '1']:
            movement.go_forward_infinite(25, 90, line_check)
        elif line_check == ['1', '0', '1', '1', '1']:
            movement.go_forward_infinite(35, 90, line_check)
        elif line_check == ['1', '1', '0', '1', '1']:
            movement.go_forward_infinite(60, 60, line_check)
        elif line_check == ['1', '1', '1', '0', '1']:
            movement.go_forward_infinite(90, 35, line_check)
        elif line_check == ['1', '1', '1', '1', '0']:
            movement.go_forward_infinite(90, 25, line_check)
        elif line_check == ['0', '0', '1', '1', '1']:
            movement.go_forward_infinite(30, 90, line_check)
        elif line_check == ['1', '0', '0', '1', '1']:
            movement.go_forward_infinite(60, 30, line_check)
        elif line_check == ['1', '1', '0', '0', '1']:
            movement.go_forward_infinite(30, 60, line_check)
        elif line_check == ['1', '1', '1', '0', '0']:
            movement.go_forward_infinite(90, 30, line_check)
        elif line_check == ['1', '1', '1', '1', '1']:
            movement.go_forward_infinite(30, 90, line_check)
        else:
            movement.go_forward(60, 0.2)

               
except KeyboardInterrupt:
    movement.pwm_low()
    GPIO.cleanup()


