def score(dice):
    
    b = [1, 2, 3, 4, 5, 6] 
    string = "".join(map(str, dice))
    score = 0
        
    # Check for triplets 
    for x in b:
        if string.count(str(x)) >= 3:
            score = x * 100 if x != 1 else x * 1000
            # delete already counted
            string = string.replace(str(x),"", 3)

    # Check for single 1s and 5s
    score += string.count(str(1)) * 100 + string.count(str(5)) * 50

    return score