"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap

throttle = gremlin.input_devices.JoystickDecorator(hotas.THR_Name,
                                                   hotas.THR_Id,
                                                   "Default")

isRolling = 0
isStrafeLeftRight = 0
isStrafeUpDown = 0
isStrafeBackward = False

def setAxes(vjoy, joy):
    global isRolling
    global isStrafeUpDown
    global isStrafeLeftRight
    global isStrafeBackward
    isFlapsDwn = joy[hotas.THR_Name].button(hotas.SWITCH_FlapsDown).is_pressed
    strafeAmt = 0 # A value 0..1
    if isFlapsDwn:
        strafeAmt = (
        joy[hotas.THR_Name].axis(hotas.THRAXIS_StrafeThrustAmt).value)
        strafeAmt = (strafeAmt * -0.5) + 0.5 # Normalize axis to 0..1
        strafeAmt = max(0.05, strafeAmt) # Clamp lower bounds to 0.25
    else:
        strafeAmt = 1.0
    vjoy[1].axis(scmap.Roll).value = strafeAmt*isRolling
    vjoy[1].axis(scmap.StrafeLeftRight).value = strafeAmt*isStrafeLeftRight
    vjoy[1].axis(scmap.StrafeUpDown).value = strafeAmt*isStrafeUpDown;
    if isStrafeBackward:
        vjoy[1].axis(scmap.StrafeForwardBack).value = strafeAmt*-1
        vjoy[1].axis(scmap.ThrottleAbs).value = 1.0 # No throttle
    else:
        fwdAmt = joy[hotas.THR_Name].axis(hotas.THRAXIS_ThrottleAbs).value
        if isFlapsDwn:
            fwdAmt = (fwdAmt * -0.5) + 0.5 # Normalize to 0..1
            vjoy[1].axis(scmap.StrafeForwardBack).value = fwdAmt
            vjoy[1].axis(scmap.ThrottleAbs).value = 1.0 # No throttle
        else:
            vjoy[1].axis(scmap.StrafeForwardBack).value = 0.0
            vjoy[1].axis(scmap.ThrottleAbs).value = fwdAmt

@throttle.axis(hotas.THRAXIS_ThrottleAbs)
def onThrottleAxis_Throttle(event, vjoy, joy):
    setAxes(vjoy, joy)

@throttle.button(hotas.SWITCH_FlapsDown)
def onThrottleSwitch_FlapsDown(event, vjoy, joy):
    setAxes(vjoy, joy)

@throttle.axis(hotas.THRAXIS_StrafeThrustAmt)
def onThrottleAxis_Slider(event, vjoy, joy):
    setAxes(vjoy, joy)

@throttle.hat(hotas.THRHAT_Roll)
def onThrottleHat_Roll(event, vjoy, joy):
    global isRolling
    isRolling = event.value[0]
    setAxes(vjoy, joy)

@throttle.hat(hotas.THRHAT_StrafeUpDown)
def onThrottleHat_StrafeUpDown(event, vjoy, joy):
    global isStrafeUpDown
    isStrafeUpDown = event.value[1]
    setAxes(vjoy, joy)

@throttle.button(hotas.THRBTN_StrafeRight)
def onThrottleBtn_StrafeRight(event, vjoy, joy):
    global isStrafeLeftRight
    isStrafeLeftRight = 1 if event.is_pressed else 0
    setAxes(vjoy, joy)

@throttle.button(hotas.THRBTN_StrafeLeft)
def onThrottleBtn_StrafeLeft(event, vjoy, joy):
    global isStrafeLeftRight
    isStrafeLeftRight = -1 if event.is_pressed else 0
    setAxes(vjoy, joy)

@throttle.button(hotas.THRBTN_StrafeBackward)
def onThrottleBtn_StrafeBackward(event, vjoy, joy):
    global isStrafeBackward
    isStrafeBackward = event.is_pressed
    setAxes(vjoy, joy)
