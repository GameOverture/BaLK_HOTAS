"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import user
import scmap

throttle = gremlin.input_devices.JoystickDecorator(user.THR_Name,
                                                   user.THR_Id,
                                                   "Default")
isMatchingVelocity = False
matchVelCnt = 0

@gremlin.input_devices.periodic(0.1)
def updateAutopilot(vjoy):
	global isMatchingVelocity
	global matchVelCnt
	if isMatchingVelocity:
		vjoy[1].button(scmap.MatchVel).is_pressed = bool(matchVelCnt == 0)
		matchVelCnt += 1
		if matchVelCnt == 10:
			matchVelCnt = 0

def cancelAutopilot(vjoy):
	global isMatchingVelocity
	global matchVelCnt
	vjoy[1].button(scmap.Autoland).is_pressed = False
	vjoy[1].button(scmap.MatchVel).is_pressed = False
	isMatchingVelocity = False
	matchVelCnt = 0

@throttle.button(user.THRBTN_AutopilotEngage)
def onThrottleBtn_AutopilotEngage(event, vjoy, joy):
	global isMatchingVelocity
	global matchVelCnt
	if event.is_pressed:
		if not joy[user.THR_Name].button(user.THRSWITCH_AutopilotPath).is_pressed:
			if joy[user.THR_Name].button(user.THRSWITCH_AutopilotAlt).is_pressed:
				isMatchingVelocity = True
				matchVelCnt = 0
		elif joy[user.THR_Name].button(user.THRSWITCH_AutopilotAlt).is_pressed:
			vjoy[1].button(scmap.Autoland).is_pressed = True
	else:
		vjoy[1].button(scmap.Autoland).is_pressed = False

@throttle.button(user.THRSWITCH_AutopilotPath)
def onThrottleSwitch_AutopilotPath(event, vjoy):
	cancelAutopilot(vjoy)

@throttle.button(user.THRSWITCH_AutopilotAlt)
def onThrottleSwitch_AutopilotAlt(event, vjoy):
	cancelAutopilot(vjoy)
