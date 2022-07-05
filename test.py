list = ["foo", "bar", "welcome"]
a = [x[::-1] if len(x) >= 5 else x for x in list]
print(" ".join(a))