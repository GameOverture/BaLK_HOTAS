"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS1
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap

joystick = gremlin.input_devices.JoystickDecorator(hotas.JOY_Name,
                                                   hotas.JOY_Id,
                                                   "Default")

throttle = gremlin.input_devices.JoystickDecorator(hotas.THR_Name,
                                                   hotas.THR_Id,
                                                   "Default")

@gremlin.input_devices.periodic(0.5)
def updateCockpit(vjoy):
    vjoy[1].button(scmap.PowerToggle).is_pressed = False

@throttle.button(hotas.THRBTN_PowerToggle)
def onJoystickBtn_ResetPowerDistribution(event, vjoy):
    vjoy[1].button(scmap.PowerToggle).is_pressed = True
