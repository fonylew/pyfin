from googlefinance import getQuotes
import json,sys

if __name__ == '__main__':
    # python test.py [STOCK SYMBOL]
    if len(sys.argv) == 2:
        print json.dumps(getQuotes('SET:' + sys.argv[1]),indent=2) 
    # return default stock (AOT)
    # indent = 2 for pretty print
    else:
        print json.dumps(getQuotes('SET:AOT'),indent=2)