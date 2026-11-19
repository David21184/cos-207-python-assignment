data = [1, 2, 3,4]
# 1. Imperative
total = 0
for x in data:
    total = total + x # x
    print("imperative :", total)
    #2 functional
    print("functional :", sum(map(lambda x: x, data)))
    #3 . Declartive
    print ("declarative:", sum(x for x in data))                      