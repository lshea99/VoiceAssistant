#!/usr/bin/python
# -*- coding:utf-8 -*-

# Author:       Lane Shea
# Created:      12/6/2021
# Last Modify:  12/7/2021
#MediaWiki can be installed from https://github.com/barrust/mediawiki

import re
from mediawiki import MediaWiki  

def sum(input):

    

    wikipedia = MediaWiki()
    # test = (input("input: "))
    # print(wikipedia.summary(test, chars = 48))
    article = wikipedia.summary(input)

    article = re.sub("\n", "", article)

    return(article)

# def wiki(text):
#    draw.display(input, 48) # 48 overwrites the default value 24
#    draw.display(wikipedia.summary(text), chars = 48))
#    draw.sleep()
