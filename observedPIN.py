import itertools

def get_pins(observed):
    
    # Dict of possible alternative digits
    keydict = {"1": "124",
               "2": "1235",
               "3": "236",
               "4": "1457",
               "5": "24568",
               "6": "3569",
               "7": "478",
               "8": "57890",
               "9": "689",
               "0": "08"}
    
    # List of all combinations of pin length
    pinlist = itertools.product("0123456789", repeat = len(observed))
    
    # List of tuples to list of strings
    pinlist = list(map("".join, pinlist))
    
    # Drop item of list if it is not in possible alternatives   
    for i in range(len(observed)):
        for pin in list(pinlist): # list(list) to remove item while iterate
            if pin[i] not in keydict[observed[i]]:
                pinlist.remove(pin)

      
    return pinlist


print(get_pins("91732"))