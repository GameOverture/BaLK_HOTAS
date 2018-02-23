"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                  BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)         
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

                          ###########################
                          # HOTAS PHYSICAL MAPPINGS #
                          ###########################

# The following variables are initialized to the physical axes and buttons on
# the HOTAS. The included scripts' logic utilize these values to know what
# inputs to "listen" for to do particular actions and maneuvers.

##############################################################################
# Joystick Information
JOY_Name = "Joystick - HOTAS Warthog"
JOY_Id = 72287234

# Set desired offset rotation amount in degrees. This is useful for those who
# have a centered joystick that are mounted in this way for ergonomic reasons
JOY_Rotation = -39

# Set the following actions to the physical axes on your joystick
JOYAXIS_Yaw = 1
JOYAXIS_Pitch = 2

##############################################################################
# Throttle Information
THR_Name = "Throttle - HOTAS Warthog"
THR_Id = 72287236

THRAXIS_ThrottleAbs = 4
THRAXIS_StrafeThrustAmt = 5            # An unused slider is a good choice.

# Set the following actions to the physical switches on the throttle. Switches
# are buttons in the virtual sense, but the logic that uses them assumes they
# can easily be held down indefinitely
THRSWITCH_FlapsDown = 23               # FLAPD (flaps down)
THRSWITCH_AutopilotPath = 27           # APALT (Autopilot switch in "PATH")
THRSWITCH_AutopilotAlt = 28            # APALT (Autopilot switch in "ALT")

# Set the following actions to the physical buttons on the throttle
THRBTN_StrafeRight = 4                 # MSR (thumb hat right)
THRBTN_StrafeLeft = 6                  # MSL (thumb hat left)
THRBTN_StrafeForward = 9               # BSF (grey two-way switch forward)
THRBTN_StrafeBackward = 10             # BSF (grey two-way switch back)
THRBTN_AutopilotEngage = 26            # APENG (Autopilot engage)

THRHAT_StrafeUpDown = 1 #HAT number 1 on the throttle (up/down, respectively)

