"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin

#################
# USER SETTINGS #
#               ##############################################################
# Your Throttle Information 
THR_Name = "Throttle - HOTAS Warthog"
THR_Id = 72287236

# Set the following actions to buttons on your throttle
THRSWITCH_FlapsDown = 23 # FLAPD (flaps down)
THRBTN_StrafeRight = 4 # MSR (thumb hat right)
THRBTN_StrafeLeft = 6 # MSL (thumb hat left)
THRBTN_StrafeForward = 9 #BSF (grey two-way switch forward)
THRBTN_StrafeBackward = 10 #BSF (grey two-way switch back)
THRHAT_StrafeUpDown = 1 #HAT number 1 on the throttle (up/down, respectively)

# Set which axis on throttle to indicate thrust amount when in 
# 'Flaps Down' mode (otherwise, it'll use 100%). A slider is a good choice.
#
# NOTE: This axis should not mapped to anything in Star Citizen
THRAXIS_StrafeThrustAmt = 5

# Star Citizen is mapped to strafe on the X, Y, and Z axes (non-rotate axis)
SCMAP_StrafeLeftRight = 1
SCMAP_StrafeUpDown = 2
SCMAP_StrafeForwardBack = 3
##############################################################################

throttle = gremlin.input_devices.JoystickDecorator(THR_Name,
                                                   THR_Id,
                                                   "Flight")

isStrafeLeftRight = 0
isStrafeUpDown = 0
isStrafeFwdBck = 0

def setStrafeAxes(vjoy, joy):
	global isStrafeUpDown
	global isStrafeLeftRight
	global isStrafeFwdBck
	thrustAmt = 0 # A value 0..1
	if joy[THR_Name].button(THRSWITCH_FlapsDown).is_pressed:
		thrustAmt = joy[THR_Name].axis(THRAXIS_StrafeThrustAmt).value
		thrustAmt = (thrustAmt * -0.5) + 0.5 # Normalize axis to 0..1
		thrustAmt = max(0.05, thrustAmt) # Clamp lower bounds to 0.25
	else:
		thrustAmt = 1.0
	vjoy[1].axis(SCMAP_StrafeLeftRight).value = thrustAmt*isStrafeLeftRight
	vjoy[1].axis(SCMAP_StrafeUpDown).value = thrustAmt*isStrafeUpDown;
	vjoy[1].axis(SCMAP_StrafeForwardBack).value = thrustAmt*isStrafeFwdBck

@throttle.button(THRSWITCH_FlapsDown)
def onThrottleTHRSWITCH_FlapsDown(event, vjoy, joy):
	setStrafeAxes(vjoy, joy)

@throttle.axis(THRAXIS_StrafeThrustAmt)
def onThrottleAxis_Slider(event, vjoy, joy):
	setStrafeAxes(vjoy, joy)

@throttle.hat(THRHAT_StrafeUpDown)
def onThrottleHat_StrafeUpDown(event, vjoy, joy):
	global isStrafeUpDown
	isStrafeUpDown = event.value[1]
	setStrafeAxes(vjoy, joy)

@throttle.button(THRBTN_StrafeRight)
def onThrottleBtn_StrafeRight(event, vjoy, joy):
	global isStrafeLeftRight
	isStrafeLeftRight = 1 if event.is_pressed else 0
	setStrafeAxes(vjoy, joy)

@throttle.button(THRBTN_StrafeLeft)
def onThrottleBtn_StrafeLeft(event, vjoy, joy):
	global isStrafeLeftRight
	isStrafeLeftRight = -1 if event.is_pressed else 0
	setStrafeAxes(vjoy, joy)

@throttle.button(THRBTN_StrafeForward)
def onThrottleBtn_StrafeForward(event, vjoy, joy):
	global isStrafeFwdBck
	isStrafeFwdBck = 1 if event.is_pressed else 0
	setStrafeAxes(vjoy, joy)

@throttle.button(THRBTN_StrafeBackward)
def onThrottleBtn_StrafeBackward(event, vjoy, joy):
	global isStrafeFwdBck
	isStrafeFwdBck = -1 if event.is_pressed else 0
	setStrafeAxes(vjoy, joy)
