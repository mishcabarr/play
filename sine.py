import math

for x in range(0, 360, 10):
    y = math.sin(math.radians(x)) * 20
    print "x=%0.1f y=%0.1f" % (x, y)
