import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# you need up to the mc line, in every minecraft program
mc = minecraft.Minecraft.create()

playerPos= mc.player.getPos()
mc.player.setPos(playerPos.x, playerPos.y + 50, playerPos.z)
playerTilePos = mc.player.getTilePos()
