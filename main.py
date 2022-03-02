import SRSP
import draw
import stocks
import news
import weather
import wiki
# import re

# This is the main function which calls on the other functions in project.
# It loops through the SRSP, the speech recognition program to read in input from speech
# And tests the values it gets against the if statements to decide on what it should do.
# Created:          11/30/2021
# Last Modified:    12/08/2021

# draw.clean()
# draw.sleep()


# draw.display(wiki.sum(SRSP.speech()),24,35)


while True:
    # break
    speechSTR = SRSP.speech()
    print(speechSTR)
    if speechSTR != None:
        speechLower = speechSTR.lower()
        
        if speechLower in ["stop", "cease", "terminate", "end", "and"]: # It can hear end as and
            # draw.clean()
            # draw.sleep()
            # break     # Commented so that it doesn't accidentally stop for the demonstration.
            print("")
        elif "clean" in speechLower:
            draw.clean()
            draw.sleep()

        elif "show me a stock" in speechLower or "stock" in speechLower:
            draw.display("What stock do you want?")
            symb = stocks.symbolLookup(SRSP.speech())
            draw.display(stocks.quoteStock(symb))

        elif "show me the weather" in speechLower or "weather" in speechLower:
            draw.display("Please say the City Name: ")
            draw.display(weather.rain(SRSP.speech()))

        elif "show me the wiki" in speechLower or "wiki" in speechLower or "wikipedia" in speechLower:
            draw.display("What article are you looking for?")
            draw.display(wiki.sum(SRSP.speech()),24,35)

        elif "show me the news" in speechLower or "news" in speechLower:
            new = news.NewsFromBBC()
            out = []
            for i in range(len(new)):
                out.append(str(new[i] + "\n"))
            out = ''.join(map(str,out))
            # print(out)
            draw.display(out, 24, 33)
            
        else: # input of "hello" draws hello
            draw.display(speechSTR)   
    else:
        print(None)
