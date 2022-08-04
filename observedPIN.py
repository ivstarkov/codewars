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

    # List of possible alternaatives
    alt_list = [keydict[x] for x in observed]
    
    # List of possible variants
    pinlist = list(itertools.product(*alt_list))

    # List of tuples to list of strings
    pinlist = list(map("".join, pinlist))
          
    return pinlist


print(get_pins("12"))