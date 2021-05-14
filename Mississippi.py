
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

var=most_frequent("mississippi")
for key in var:
    print(key,"=",var[key])
    print ("\n")
