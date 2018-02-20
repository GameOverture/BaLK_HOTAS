import gremlin

##############################################################################

##############################################################################


throttle = gremlin.input_devices.JoystickDecorator("Throttle - HOTAS Warthog",
                                                   72287236,
                                                   "Flight")

def updateStrafeAxes(vjoy, joy):
	global isStrafeUpDown
	global isStrafeLeftRight
	global isStrafeFwdBck
	thrustAmt = 0 # A value 0..1
	if joy["Throttle - HOTAS Warthog"].button(KEY_FlapsDown).is_pressed:
		thrustAmt = joy["Throttle - HOTAS Warthog"].axis(USER_THROTTLE_SLIDERAXIS).value
		thrustAmt = (thrustAmt * -0.5) + 0.5 # Normalize axis to 0..1
		thrustAmt = max(0.25, thrustAmt) # Clamp lower bounds to 0.25
	else:
		thrustAmt = 1.0
	vjoy[1].axis(USER_STRAFE_XAXIS).value = thrustAmt*isStrafeLeftRight
	vjoy[1].axis(USER_STRAFE_YAXIS).value = thrustAmt*isStrafeUpDown;
	vjoy[1].axis(USER_STRAFE_ZAXIS).value = thrustAmt*isStrafeFwdBck

@throttle.button(KEY_FlapsDown)
def flapsDownTriggered(event, vjoy, joy):
	updateStrafeAxes(vjoy, joy)

@throttle.axis(USER_THROTTLE_SLIDERAXIS)
def throttleSlider(event, vjoy, joy):
	updateStrafeAxes(vjoy, joy)

# STRAFE INPUT CALLBACKS -----------------------------------------------------
@throttle.hat(1)
def strafeUpDown(event, vjoy, joy):
	global isStrafeUpDown
	isStrafeUpDown = event.value[1]
	updateStrafeAxes(vjoy, joy)

@throttle.button(USER_KEY_STRAFE_RIGHT)
def strafeRight(event, vjoy, joy):
	global isStrafeLeftRight
	isStrafeLeftRight = 1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)

@throttle.button(USER_KEY_STRAFE_LEFT)
def strafeLeft(event, vjoy, joy):
	global isStrafeLeftRight
	isStrafeLeftRight = -1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)

@throttle.button(USER_KEY_STRAFE_FORWARD)
def strafeForward(event, vjoy, joy):
	global isStrafeFwdBck
	isStrafeFwdBck = 1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)

@throttle.button(USER_KEY_STRAFE_BACKWARD)
def strafeBack(event, vjoy, joy):
	global isStrafeFwdBck
	isStrafeFwdBck = -1 if event.is_pressed else 0
	updateStrafeAxes(vjoy, joy)
