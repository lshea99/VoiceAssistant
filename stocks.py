#!/usr/bin/python
# -*- coding:utf-8 -*-

# Author:       Preston Dulion
# Created:      11/28/2021
# Last Modify:  12/07/2021

# import draw
import re
import finnhub
from datetime import datetime
finnhub_client = finnhub.Client(api_key="c17tkqf48v6reqlb36lg")
# stock = "O"
# print(finnhub_client.quote('AAPL'))

def symbolLookup(input):
    value = finnhub_client.symbol_lookup(input)

    # print(value)

    return(value["result"][0]["displaySymbol"])

def quoteStock(stock):
    quote = finnhub_client.quote(stock)

    curPrice    = quote["c"]
    change      = quote["d"]
    # percChange  = quote["dp"]
    high        = quote["h"]
    low         = quote["l"]
    open        = quote["o"]
    # prevClose   = quote["pc"]
    time        = str(datetime.fromtimestamp(int(quote["t"])))

    write =  f"Symbol: {stock}\n"
    write += f"Current Price: {curPrice}\n"
    write += f"Change: {change}\n"
    write += f"High: {high}\n"
    write += f"Low: {low}\n"
    write += f"Open: {open}\n"
    write += f"Timestamp: {time}"

    # print(write)
    return(write)