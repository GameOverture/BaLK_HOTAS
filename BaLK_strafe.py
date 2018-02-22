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
# Thrustmaster Warthog decorator
DECOR_ThrottleName = "Throttle - HOTAS Warthog"
DECOR_ThrottleId = 72287236

# Set the following actions to buttons on your throttle
SWITCH_FlapsDown = 23 # FLAPD (flaps down)
BTN_StrafeRight = 4 # MSR (thumb hat right)
BTN_StrafeLeft = 6 # MSL (thumb hat left)
BTN_StrafeForward = 9 #BSF (grey two-way switch forward)
BTN_StrafeBackward = 10 #BSF (grey two-way switch back)
HAT_StrafeUpDown = 1 #HAT number 1 on the throttle (up and down, respectively)

# Star Citizen is mapped to strafe on the X, Y, and Z axes (non-rotate axis)
SCAXIS_StrafeLeftRight = 1
SCAXIS_StrafeUpDown = 2
SCAXIS_StrafeForwardBack = 3

# Set axis '5' on throttle (which is the grey slider on the Warthog HOTAS) to 
# indicate thrust amount when in Flaps mode (otherwise, it'll use 100%)
THROTTLE_AxisSlider = 5
##############################################################################

throttle = gremlin.input_devices.JoystickDecorator(DECOR_ThrottleName,
                                                   DECOR_ThrottleId,
                                                   "Flight")

isStrafeLeftRight = 0
isStrafeUpDown = 0
isStrafeFwdBck = 0

def updateStrafeAxes(vjoy, joy):
	global isStrafeUpDown
	global isStrafeLeftRight
	global isStrafeFwdBck
	thrustAmt = 0 # A value 0..1
	if joy[DECOR_ThrottleName].button(SWITCH_FlapsDown).is_pressed:
		thrustAmt = joy[DECOR_ThrottleName].axis(THROTTLE_AxisSlider).value
		thrustAmt = (thrustAmt * -0.5) + 0.5 # Normalize axis to 0..1
		thrustAmt = max(0.05, thrustAmt) # Clamp lower bounds to 0.25
	else:
		thrustAmt = 1.0
	vjoy[1].axis(SCAXIS_StrafeLeftRight).value = thrustAmt*isStrafeLeftRight
	vjoy[1].axis(SCAXIS_StrafeUpDown).value = thrustAmt*isStrafeUpDown;
	vjoy[1].axis(SCAXIS_StrafeForwardBack).value = thrustAmt*isStrafeFwdBck

@throttle.button(SWITCH_FlapsDown)
def flapsDownTriggered(event, vjoy, joy):
	updateStrafeAxes(vjoy, joy)

@throttle.axis(THROTTLE_AxisSlider)
def throttleSlider(event, vjoy, joy):
	updateStrafeAxes(vjoy, joy)

@throttle.hat(HAT_StrafeUpDown)
def strafeUpDown(event, vjoy, joy):
	global isStrafeUpDown
	isStrafeUpDown = event.value[1]
	updateStrafeAxes(vjoy, joy)

@throttle.button(BTN_StrafeRight)
def strafeRight(event, vjoy, joy):
	global isStrafeLeftRight
	isStrafeLeftRight = 1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)

@throttle.button(BTN_StrafeLeft)
def strafeLeft(event, vjoy, joy):
	global isStrafeLeftRight
	isStrafeLeftRight = -1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)

@throttle.button(BTN_StrafeForward)
def strafeForward(event, vjoy, joy):
	global isStrafeFwdBck
	isStrafeFwdBck = 1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)

@throttle.button(BTN_StrafeBackward)
def strafeBack(event, vjoy, joy):
	global isStrafeFwdBck
	isStrafeFwdBck = -1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)
