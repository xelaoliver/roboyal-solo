import discord

#------- 
# All the emoji are stored here, if you want to use your own, you can replace them here.
# You can also use the supplied custom emoji by uploading them to your own server"
# or just use standard Emoji
#-------

class PlayerAction:
    # up  = 0, right = 1, down = 2, left = 3
    direction = 0
    name = ""
    id = 0
    movement = True
    custom  = True
    
    def __init__(self, direction, name, id, movement):
        self.direction = direction
        self.name = name
        self.id = id
        self.movement = movement

    def StringMessage(this):
        if(this.custom):
            return "<:" + this.name + ":" + str(this.id) + ">"
        else:
            return ":" + this.name + ":"

# the available actions to choose from
actions = [ 
    PlayerAction(direction = 3, name = "Robo_Player_Left",  id = 1410589572466737233, movement = True ),
    PlayerAction(direction = 0, name = "Robo_Player_Up",    id = 1410589598941446235, movement = True ),
    PlayerAction(direction = 2, name = "Robo_Player_Down",  id = 1410589583942488256, movement = True ),
    PlayerAction(direction = 1, name = "Robo_Player_Right", id = 1410589591462744136, movement = True ),
    PlayerAction(direction = 0, name = "Robo_Player_Punch", id = 1410590895052427365, movement = False ),
]

# the different states of the robots
# up  = 0, right = 1, down = 2, left = 3

playerDirections = [
    "<:Robo_Player_Up:1410589598941446235>",
    "<:Robo_Player_Right:1410589591462744136>",
    "<:Robo_Player_Down:1410589583942488256>",
    "<:Robo_Player_Left:1410589572466737233>",
]
damagedPlayerDirections = [
    "<:Robo_Player_Up_Broken:1410589563503509514>",
    "<:Robo_Player_Right_Broken:1410589554720903208>",
    "<:Robo_Player_Down_Broken:1410589547183739060>",
    "<:Robo_Player_Left_Broken:1410589538862235689>"
]

npcDirections = [
    "<:Robo_Bot_Up:1410589530758844416>",
    "<:Robo_Bot_Right:1410589522797924434>",
    "<:Robo_Bot_Down:1410589513385771028>",
    "<:Robo_Bot_Left:1410589505026658415>"
]
damagedNpcDirections = [
    "<:Robo_Bot_Up_Broken:1410589495253930017>",
    "<:Robo_Bot_Right_Broken:1410589485879529503>",
    "<:Robo_Bot_Down_Broken:1410589474458701956>",
    "<:Robo_Bot_Left_Broken:1410589436550320184>"
]
#the emote for a dead, but not destroyed body
deadBot = "❌"

#the floortile is a single character universal emoji to greatly reduce the character count in the embed message.
#this way, the grids can be much larger before hitting the 2048 character limit
floorTile = "◻️"

#cosmetic emotes
redBot = "<:RoboYalRed:1410592745222836274>"
blueBot = "<:RoboYalBlue:1410592735827853313>"

