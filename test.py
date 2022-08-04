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
    pinlist = list(itertools.combinations_with_replacement("1234567890", len(observed)))
    
    # Drop item of list if it is not in possible alternatives   
    for i in range(len(observed)):
        print(pinlist)
        for pin in pinlist:
            print(pin)
            print(keydict[observed[i]])
            
            if pin[i] not in keydict[observed[i]]:
                print("=======")
                print("drop" + str(pin))
                print("=======")
            #    pinlist.remove(pin)
           
    return pinlist


print(get_pins("8"))