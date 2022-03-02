#!/usr/bin/python
# -*- coding:utf-8 -*-

# Author:       Preston Dulion
# Created:      11/28/2021
# Last Modify:  11/28/2021

import draw # <- this sends it to the e-ink display. COMMENT THIS OUT IF YOUR TESTING.

# !!! This is outdated no include in final submission @me >:(

def example(input = "Hello, World!"):
    # It ONLY accepts String. If its any other datatype, it'll error.
    draw.display(input, 48) # 48 overwrites the default value 24 # the 48 and 24 are meant to be font size - PTD - 12/8
    # It clears on call, so 'Hello!' will remain until its next called.

    # Newline stuff works as well.
    draw.display("Hello\nWorld!")

    # Any num input
    # draw.clean(0)

    # draw.display("AAAABAAAABAAAABAAAABAAAAB-")
    # draw.display("A\nA\nA\nA\nB\nA\nA\nA\nA\nB\n|")
    draw.display("AAAABAAAABAAAABAAAABAAAAB-\nA\nA\nA\nB\nA\nA\nA\nA\nB\n|") # 1 less A in the column test because its already used in the first row
    # 26 x 11 with font size 24
    draw.clean()
    draw.sleep()
    return(0)