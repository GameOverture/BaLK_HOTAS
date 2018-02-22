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
THRBTN_AutopilotEngage = 26 # APENG (Autopilot engage)
THRSWITCH_AutopilotPath = 27 # APALT (Autopilot switch in "PATH")
THRSWITCH_AutopilotAlt = 28 # APALT (Autopilot switch in "ALT")

# Star Citizen is mapped to use the following joystick buttons
SCMAP_Autoland = 10
SCMAP_MatchVel = 11
##############################################################################

throttle = gremlin.input_devices.JoystickDecorator(THR_Name,
                                                   THR_Id,
                                                   "Flight")
isMatchingVelocity = False
matchVelCnt = 0

@gremlin.input_devices.periodic(0.1)
def updateAutopilot(vjoy):
	global isMatchingVelocity
	global matchVelCnt
	if isMatchingVelocity:
		vjoy[1].button(SCMAP_MatchVel).is_pressed = bool(matchVelCnt == 0)
		matchVelCnt += 1
		if matchVelCnt == 10:
			matchVelCnt = 0

def cancelAutopilot(vjoy):
	global isMatchingVelocity
	global matchVelCnt
	vjoy[1].button(SCMAP_Autoland).is_pressed = False
	vjoy[1].button(SCMAP_MatchVel).is_pressed = False
	isMatchingVelocity = False
	matchVelCnt = 0

@throttle.button(THRBTN_AutopilotEngage)
def onThrottleBtn_AutopilotEngage(event, vjoy, joy):
	global isMatchingVelocity
	global matchVelCnt
	if event.is_pressed
		if not joy[THR_Name].button(THRSWITCH_AutopilotPath).is_pressed
		and if joy[THR_Name].button(THRSWITCH_AutopilotAlt).is_pressed:
			isMatchingVelocity = True
			matchVelCnt = 0
		elif joy[THR_Name].button(THRSWITCH_AutopilotAlt).is_pressed:
			vjoy[1].button(SCMAP_Autoland).is_pressed = True
	else:
		vjoy[1].button(SCMAP_Autoland).is_pressed = False

@throttle.button(THRSWITCH_AutopilotPath)
def onThrottleSwitch_AutopilotPath(event, vjoy):
	cancelAutopilot(vjoy)

@throttle.button(THRSWITCH_AutopilotAlt)
def onThrottleSwitch_AutopilotAlt(event, vjoy):
	cancelAutopilot(vjoy)
