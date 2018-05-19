"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                              2018 Jason Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap

g13 = gremlin.input_devices.JoystickDecorator("Logitech G13 Joystick",
                                              74302123,
                                              "Default")
                                              
if hotas.USING_RUDDER_PEDALS:
    rudders = gremlin.input_devices.JoystickDecorator(hotas.RUD_Name,
                                                      hotas.RUD_Id,
                                                      "Default")

invertForwardBack = -1.0 # must be -1.0 or 1.0 (negative for invert)
g13Deadzone = 0.1

@g13.axis(1)
def onG13Axis_Yaw(event, vjoy):
    if event.value >= g13Deadzone or event.value <= -g13Deadzone:
        vjoy[1].axis(scmap.StrafeLeftRight).value = event.value
    else:
        vjoy[1].axis(scmap.StrafeLeftRight).value = 0.0

@g13.axis(2)
def onG13Axis_Pitch(event, vjoy):
    if event.value >= g13Deadzone or event.value <= -g13Deadzone:
        vjoy[1].axis(scmap.StrafeForwardBack).value = event.value * invertForwardBack
    else:
        vjoy[1].axis(scmap.StrafeForwardBack).value = 0.0

if hotas.USING_RUDDER_PEDALS:
    @rudders.axis(hotas.RUDAXIS_Reverse)
    def onRudderAxisBtn_LeftTowBreak(event, vjoy, joy):
        if joy[hotas.THR_Name].button(hotas.SWITCH_Power).is_pressed:
            pass

if hotas.USING_RUDDER_PEDALS:
    @rudders.axis(hotas.RUDAXIS_Boost)
    def onRudderAxisBtn_RightTowBreak(event, vjoy, joy):
        if joy[hotas.THR_Name].button(hotas.SWITCH_Power).is_pressed:
            pass


