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
# Thrustmaster Warthog decorator
DECOR_JoystickName = "Joystick - HOTAS Warthog"
DECOR_JoystickId = 72287234

# Desired rotation amount in degrees
JOYSTICK_Rotation = -39
##############################################################################

joystick = gremlin.input_devices.JoystickDecorator(DECOR_JoystickName,
                                                   DECOR_JoystickId,
                                                   "Flight")

radians = math.radians(JOYSTICK_Rotation)
cosX = math.cos(radians);
sinX = -math.sin(radians);
cosY = math.cos(radians);
sinY = math.sin(radians);

actualX = 0
actualY = 0

def maxVectorLength(angle):
	angle = abs(angle)
	if 0 <= angle < math.pi/4:
		return math.sqrt(1 + math.tan(angle)**2)
	elif math.pi/4 <= angle < 0.75*math.pi:
		return math.sqrt(1 + (1.0/math.tan(angle)) ** 2)
	else:
		return math.sqrt(1 + math.tan(angle) ** 2)

@USER_JOY.axis(1)
def yaw(event, vjoy):
	global actualX
	global actualY
	actualX = event.value
	gremlin.util.log(actualX)
	vjoy[1].axis(4).value = actualX*cosX + actualY*sinX
	vjoy[1].axis(5).value =	-actualX*sinX + actualY*cosX

@USER_JOY.axis(2)
def pitch(event, vjoy):
	global actualX
	global actualY
	actualY = event.value
	vjoy[1].axis(5).value = actualY*cosY + actualX*sinY
	vjoy[1].axis(4).value = -actualY*sinY + actualX*cosY
