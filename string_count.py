def count(string):
    return {x: string.count(x) for x in string}

print(count("abcdab"))