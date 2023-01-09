def isISO(x,y):
    if len(x)!=len(y):
        return false
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return false
    return true
print(isISO("fool","poor"))
print(isISO("faol","poor"))
print(isISO("too","bar"))
print(isISO("toto","yaya"))
