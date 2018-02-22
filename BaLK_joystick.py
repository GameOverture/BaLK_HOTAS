"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import math

#################
# USER SETTINGS #
#               ##############################################################
# Your Joystick Information 
JOY_Name = "Joystick - HOTAS Warthog"
JOY_Id = 72287234
JOY_Rotation = -39 # Desired rotation amount in degrees (for ergonomic grip)

# Set the following actions to axes on your joystick
JOYAXIS_Yaw = 1
JOYAXIS_Pitch = 2

# Star Citizen is mapped to yaw and pitch on the X-Rot, and Y-Rot axes 
SCMAP_Yaw = 4
SCMAP_Pitch = 5
##############################################################################

joystick = gremlin.input_devices.JoystickDecorator(JOY_Name,
                                                   JOY_Id,
                                                   "Flight")

radians = math.radians(JOY_Rotation)
cosX = math.cos(radians);
sinX = -math.sin(radians);
cosY = math.cos(radians);
sinY = math.sin(radians);

actualX = 0
actualY = 0

# Thank you to @WhiteMagic for these math formulas
def maxVectorLength(angle):
	angle = abs(angle)
	if 0 <= angle < math.pi/4:
		return math.sqrt(1 + math.tan(angle)**2)
	elif math.pi/4 <= angle < 0.75*math.pi:
		return math.sqrt(1 + (1.0/math.tan(angle)) ** 2)
	else:
		return math.sqrt(1 + math.tan(angle) ** 2)

@joystick.axis(JOYAXIS_Yaw)
def onJoystickAxis_X(event, vjoy):
	global actualX
	global actualY
	actualX = event.value
	gremlin.util.log(actualX)
	vjoy[1].axis(SCMAP_Yaw).value = actualX*cosX + actualY*sinX
	vjoy[1].axis(SCMAP_Pitch).value = -actualX*sinX + actualY*cosX

@joystick.axis(JOYAXIS_Pitch)
def onJoystickAxis_Y(event, vjoy):
	global actualX
	global actualY
	actualY = event.value
	vjoy[1].axis(SCMAP_Pitch).value = actualY*cosY + actualX*sinY
	vjoy[1].axis(SCMAP_Yaw).value = -actualY*sinY + actualX*cosY
