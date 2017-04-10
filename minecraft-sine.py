import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

# you need up to the mc line, in every minecraft program
mc = minecraft.Minecraft.create()

z_start = -155
z_end = 155

step = 6
ybase = 40
sine_multiplier = 20
block_type = block.DIAMOND_ORE

for z in range(z_start, z_end):
    mc.postToChat("z = " + str(z))

    for x in range(0, 720, step):
        y = math.sin(math.radians(x)) * (sine_multiplier +z) + ybase
        xpos = x/step - (360/step)

        # print "xpos=%0.1f y=%0.1f z=%0.1f" % (xpos, y, z)
        mc.setBlock(xpos, y, z, block_type)
        # time.sleep(0.1)
