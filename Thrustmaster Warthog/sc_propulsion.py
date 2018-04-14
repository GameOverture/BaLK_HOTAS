"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                              2018 Jason Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap

throttle = gremlin.input_devices.JoystickDecorator(hotas.THR_Name,
                                                   hotas.THR_Id,
                                                   "Default")
                                                   
if hotas.USING_RUDDER_PEDALS:
    rudders = gremlin.input_devices.JoystickDecorator(hotas.RUD_Name,
                                                      hotas.RUD_Id,
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
    if not hotas.USING_RUDDER_PEDALS:
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

@throttle.button(hotas.THRBTN_StrafeUp)
def onThrottleBtn_StrafeUp(event, vjoy, joy):
    global isStrafeUpDown
    isStrafeUpDown = 1 if event.is_pressed else 0
    setAxes(vjoy, joy)

@throttle.button(hotas.THRBTN_StrafeDown)
def onThrottleBtn_StrafeDown(event, vjoy, joy):
    global isStrafeUpDown
    isStrafeUpDown = -1 if event.is_pressed else 0
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

if hotas.USING_RUDDER_PEDALS:
    @rudders.axis(hotas.RUDAXISBTN_BrakeReverse)
    def onRudderAxisBtn_BrakeReverse(event, vjoy):
        if event.value >= hotas.RUDAXISBTN_Threshold:
            vjoy[1].button(scmap.SpaceBrake).is_pressed = True
        else:
            vjoy[1].button(scmap.SpaceBrake).is_pressed = False

if hotas.USING_RUDDER_PEDALS:
    @rudders.axis(hotas.RUDAXISBTN_Boost)
    def onRudderAxisBtn_Boost(event, vjoy):
        if event.value >= hotas.RUDAXISBTN_Threshold:
            vjoy[1].button(scmap.Boost).is_pressed = True
        else:
            vjoy[1].button(scmap.Boost).is_pressed = False

if hotas.USING_RUDDER_PEDALS:
    @rudders.axis(hotas.RUDAXIS_Roll)
    def onRudderAxis_Rudders(event, vjoy):
        vjoy[1].axis(scmap.Roll).value = event.value * hotas.RUDDER_PEDALS_INVERT
        
@throttle.button(hotas.THRBTN_LandingGearQuantum)
def onThrottleBtn_LandingGearQuantum(event, vjoy, joy):
    if event.is_pressed:
        if joy[hotas.THR_Name].button(hotas.SWITCH_FlapsDown).is_pressed:
            vjoy[1].button(scmap.LandingGear).is_pressed = True
        else:
            vjoy[1].button(scmap.Quantum).is_pressed = True
    else:
        vjoy[1].button(scmap.LandingGear).is_pressed = False
        vjoy[1].button(scmap.Quantum).is_pressed = False

@throttle.button(hotas.THRBTN_Afterburner)
def onThrottleBtn_Afterburner(event, vjoy):
    vjoy[1].button(scmap.Afterburner).is_pressed = event.is_pressed
    
@throttle.button(hotas.THRBTN_DecoupledModeToggle)
def onThrottleBtn_DecoupledModeToggle(event, vjoy):
    vjoy[1].button(scmap.DecoupledMode).is_pressed = event.is_pressed