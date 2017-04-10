a = 0
b = 1
print a
print b
answer = a+b

while answer < 10000000:
    print answer
    a = b
    b = answer
    answer = a + b
