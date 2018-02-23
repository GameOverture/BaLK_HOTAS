"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import math
import user
import scmap

joystick = gremlin.input_devices.JoystickDecorator(user.JOY_Name,
                                                   user.JOY_Id,
                                                   "Default")

radians = math.radians(user.JOY_Rotation)
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

@joystick.axis(user.JOYAXIS_Yaw)
def onJoystickAxis_X(event, vjoy):
	global actualX
	global actualY
	actualX = event.value
	gremlin.util.log(actualX)
	vjoy[1].axis(scmap.Yaw).value = actualX*cosX + actualY*sinX
	vjoy[1].axis(scmap.Pitch).value = -actualX*sinX + actualY*cosX

@joystick.axis(user.JOYAXIS_Pitch)
def onJoystickAxis_Y(event, vjoy):
	global actualX
	global actualY
	actualY = event.value
	vjoy[1].axis(scmap.Pitch).value = actualY*cosY + actualX*sinY
	vjoy[1].axis(scmap.Yaw).value = -actualY*sinY + actualX*cosY
