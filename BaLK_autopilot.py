import gremlin

##############################################################################
BTN_AutopilotEngage = 26 # APENG (Autopilot engage)
SWITCH_AutopilotPath = 27 # APALT (Autopilot switch in "PATH")
SWITCH_AutopilotAlt = 28 # APALT (Autopilot switch in "ALT")

# Star Citizen is mapped to use the following joystick buttons
SCMAP_Autoland = 10
SCMAP_MatchTargetVelocity = 11
##############################################################################

isMatchingVelocity = False
matchingVelocityPulseCount = 0

throttle = gremlin.input_devices.JoystickDecorator("Throttle - HOTAS Warthog",
                                                   72287236,
                                                   "Flight")

@gremlin.input_devices.periodic(0.1)
def updateSwitches(vjoy):
	global isMatchingVelocity
	global matchingVelocityPulseCount
	if isMatchingVelocity:
		vjoy[1].button(SCMAP_MatchTargetVelocity).is_pressed = bool(matchingVelocityPulseCount == 0)
		matchingVelocityPulseCount += 1
		if matchingVelocityPulseCount == 10:
			matchingVelocityPulseCount = 0

@throttle.button(BTN_AutopilotEngage)
def autopilotEngage(event, vjoy, joy):
	global isMatchingVelocity
	global matchingVelocityPulseCount
	if event.is_pressed
		if not joy["Throttle - HOTAS Warthog"].button(SWITCH_AutopilotPath).is_pressed and if joy["Throttle - HOTAS Warthog"].button(SWITCH_AutopilotAlt).is_pressed:
			isMatchingVelocity = True
			matchingVelocityPulseCount = 0
		elif joy["Throttle - HOTAS Warthog"].button(SWITCH_AutopilotAlt).is_pressed:
			vjoy[1].button(SCMAP_Autoland).is_pressed = True
	else:
		vjoy[1].button(SCMAP_Autoland).is_pressed = False

def cancelAutopilot(vjoy):
	global isMatchingVelocity
	global matchingVelocityPulseCount
	vjoy[1].button(SCMAP_Autoland).is_pressed = False
	vjoy[1].button(SCMAP_MatchTargetVelocity).is_pressed = False
	isMatchingVelocity = False
	matchingVelocityPulseCount = 0

@throttle.button(SWITCH_AutopilotPath)
def autopilotSwitchPath(event, vjoy):
	cancelAutopilot(vjoy)

@throttle.button(SWITCH_AutopilotAlt)
def autopilotSwitchPath(event, vjoy):
	cancelAutopilot(vjoy)