import gremlin
import math

##############################################################################
# Desired rotation amount in degrees
USER_ROTATION = -39

# Joystick decorator 
USER_JOY = gremlin.input_devices.JoystickDecorator("Joystick - HOTAS Warthog",
                                                   72287234,
                                                   "Flight")
##############################################################################

radians = math.radians(USER_ROTATION)
cosX = math.cos(radians);
sinX = -math.sin(radians);
cosY = math.cos(radians);
sinY = math.sin(radians);

actualX = 0
actualY = 0

scale = 2 / math.log(2) * math.log(math.fabs(math.cos(radians) + math.fabs(math.sin(radians))))
#pow(1.41, scale)


@USER_JOY.axis(1)
def yaw(event, vjoy):
    global actualX
    global actualY
    actualX = event.value
    gremlin.util.log(actualX)
    vjoy[1].axis(4).value = actualX*cosX + actualY*sinX
    vjoy[1].axis(5).value =	-actualX*sinX + actualY*cosX
    
@USER_JOY.axis(2)
def pitch(event, vjoy):
    global actualX
    global actualY
    actualY = event.value
    vjoy[1].axis(5).value = actualY*cosY + actualX*sinY
    vjoy[1].axis(4).value = -actualY*sinY + actualX*cosY
