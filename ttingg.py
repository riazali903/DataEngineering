

a = [1,2,3,4,5]

def fun(x):
    return x + 3

def odd(x):
    for i in x:
     print(i>2)


# d =list(map(fun,a))
#
#e = list(filter(odd,a))

c = odd(a)
print(c)
import json
json.dumps(None,indent=)