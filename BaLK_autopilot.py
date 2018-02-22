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
BTN_AutopilotEngage = 26 # APENG (Autopilot engage)
SWITCH_AutopilotPath = 27 # APALT (Autopilot switch in "PATH")
SWITCH_AutopilotAlt = 28 # APALT (Autopilot switch in "ALT")

# Star Citizen is mapped to use the following joystick buttons
SCMAP_Autoland = 10
SCMAP_MatchVel = 11
##############################################################################

throttle = gremlin.input_devices.JoystickDecorator(DECOR_ThrottleName,
                                                   DECOR_ThrottleId,
                                                   "Flight")
isMatchingVelocity = False
matchVelCnt = 0

@gremlin.input_devices.periodic(0.1)
def updateSwitches(vjoy):
	global isMatchingVelocity
	global matchVelCnt
	if isMatchingVelocity:
		vjoy[1].button(SCMAP_MatchVel).is_pressed = bool(matchVelCnt == 0)
		matchVelCnt += 1
		if matchVelCnt == 10:
			matchVelCnt = 0

@throttle.button(BTN_AutopilotEngage)
def autopilotEngage(event, vjoy, joy):
	global isMatchingVelocity
	global matchVelCnt
	if event.is_pressed
		if not joy[DECOR_ThrottleName].button(SWITCH_AutopilotPath).is_pressed
		and if joy[DECOR_ThrottleName].button(SWITCH_AutopilotAlt).is_pressed:
			isMatchingVelocity = True
			matchVelCnt = 0
		elif joy[DECOR_ThrottleName].button(SWITCH_AutopilotAlt).is_pressed:
			vjoy[1].button(SCMAP_Autoland).is_pressed = True
	else:
		vjoy[1].button(SCMAP_Autoland).is_pressed = False

def cancelAutopilot(vjoy):
	global isMatchingVelocity
	global matchVelCnt
	vjoy[1].button(SCMAP_Autoland).is_pressed = False
	vjoy[1].button(SCMAP_MatchVel).is_pressed = False
	isMatchingVelocity = False
	matchVelCnt = 0

@throttle.button(SWITCH_AutopilotPath)
def autopilotSwitchPath(event, vjoy):
	cancelAutopilot(vjoy)

@throttle.button(SWITCH_AutopilotAlt)
def autopilotSwitchPath(event, vjoy):
	cancelAutopilot(vjoy)