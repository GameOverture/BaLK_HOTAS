"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                          2018 Jason "BaLK" Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

                            #################
                            # USER SETTINGS #
                            #################

# Your Joystick Information 
JOY_Name = "Joystick - HOTAS Warthog"
JOY_Id = 72287234
JOY_Rotation = -39 # Desired rotation amount in degrees (for ergonomic grip)

# Set the following actions to axes on your joystick
JOYAXIS_Yaw = 1
JOYAXIS_Pitch = 2

# Your Throttle Information 
THR_Name = "Throttle - HOTAS Warthog"
THR_Id = 72287236

# Set the following actions to buttons on your throttle
THRSWITCH_FlapsDown = 23 # FLAPD (flaps down)
THRBTN_StrafeRight = 4 # MSR (thumb hat right)
THRBTN_StrafeLeft = 6 # MSL (thumb hat left)
THRBTN_StrafeForward = 9 #BSF (grey two-way switch forward)
THRBTN_StrafeBackward = 10 #BSF (grey two-way switch back)
THRHAT_StrafeUpDown = 1 #HAT number 1 on the throttle (up/down, respectively)
THRBTN_AutopilotEngage = 26 # APENG (Autopilot engage)
THRSWITCH_AutopilotPath = 27 # APALT (Autopilot switch in "PATH")
THRSWITCH_AutopilotAlt = 28 # APALT (Autopilot switch in "ALT")

# Set which axis on throttle to indicate thrust amount when in 
# 'Flaps Down' mode (otherwise, it'll use 100%). A slider is a good choice.
#
# NOTE: This axis should not mapped to anything in Star Citizen
THRAXIS_StrafeThrustAmt = 5

