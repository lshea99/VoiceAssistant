#!/usr/bin/python
# -*- coding:utf-8 -*-

# Author:       Preston Dulion
# Created:      11/28/2021
# Last Modify:  11/28/2021
# Editted from example obtained here: https://github.com/waveshare/e-Paper

import sys
import os
import re

picdir = 'libnpic/pic'
libdir = 'libnpic/waveshare_epd'
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from libnpic.waveshare_epd import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
logging.basicConfig(level=logging.DEBUG)

def clean():

    try:
        logging.info("epd4in2 draw.clean")
        
        epd = epd4in2.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2.epdconfig.module_exit()
        exit()

    return(0)

def sleep():

    try:
        logging.info("epd4in2 draw.sleep")
        
        epd = epd4in2.EPD()
        logging.info("init")
        epd.init()

        # epd.Clear()
        logging.info("Goto Sleep...")
        epd.sleep()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2.epdconfig.module_exit()
        exit()
    return(0)

def display(inputText, fontSize = 24, newLineOnCharacterCount = 0): # fontSize = 24 is a default value, will be overwritten
    num = newLineOnCharacterCount
    if "\n" in inputText:
        regx = regx = "(\\n.{"+str(num)+"})"
    else: # ^ splits after every num charcters AFTER a \n
          # v splits after every num characters regardless of a \n
        regx = "(\\n?.{"+str(num)+"})"
    if num != 0:
        # if "\n" not in inputText:
            # Splits the line every num characters   
            if fontSize < 25 and fontSize > 13:
                num = 30
            elif fontSize < 13:
                num = 55

            inputText = re.sub(regx, "\\1\n", inputText, 0, re.DOTALL)


    try:
        logging.info("epd4in2 draw.display")
        
        epd = epd4in2.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()
        
        fontStyle = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), fontSize)
        
        # Drawing on the Horizontal image
        logging.info("Drawing:\n" + inputText)
        Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)

        draw.text((10, 0), inputText, font = fontStyle, fill = 0)

        epd.display(epd.getbuffer(Himage))
        
        time.sleep(2)

        # # epd.Clear()
        # logging.info("Goto Sleep...")
        # epd.sleep()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd4in2.epdconfig.module_exit()
        exit()
    return(0)