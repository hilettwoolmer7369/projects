### basic teleporter

import mcpi.minecraft as mc, time # imports mcpi modules
game = mc.Minecraft.create() # connects to a minecraft game and calls it game

time.sleep(10)
game.postToChat("Hey there nerd, you are about to be teleported")
time.sleep(3)
game.player.setPos( 69, 69, 69)
time.sleep(1)
game.postToChat ("Hey did you enjoy that? good because here we go again")
time.sleep(2)
game.player.setPos(60, 18, 77)
game.postToChat ("well that was fun now go build me a castle")

