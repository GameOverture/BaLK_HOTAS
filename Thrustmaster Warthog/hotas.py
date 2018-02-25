"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 BaLK HOTAS
              (Joystick Gremlin Profile/Scripts for Star Citizen)

                              2018 Jason Knobler
          (https://robertsspaceindustries.com/citizens/Game_Overture)         
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

                          ###########################
                          # HOTAS PHYSICAL MAPPINGS #
                          ###########################

# The following variables are initialized to the physical axes and buttons on
# the HOTAS. The included scripts' logic utilize these values to know what
# inputs to "listen" for to do particular actions and maneuvers.

USING_RUDDER_PEDALS = True

##############################################################################
# Rudder Pedals Information
RUD_Name = "Mad Catz Pro Flight Combat Rudder Pedals"
RUD_Id = 111347556

# Set the following actions to the physical axes on your joystick
RUDAXIS_LeftToe = 1
RUDAXIS_RightToe = 2
RUDAXIS_Rudder = 3

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

JOYBTN_FireWep = 1                     # TG1 (Trigger stage 1)
JOYBTN_FocusFireZoom = 6               # TG2 (Trigger stage 2)
JOYBTN_CycleWepGrp = 3                 # S3 (pinky button)
JOYBTN_Missiles = 2                    # S2 (red button)
JOYBTN_CounterMeasures = 5             # S1 (index finger button)

##############################################################################
# Throttle Information
THR_Name = "Throttle - HOTAS Warthog"
THR_Id = 72287236

THRAXIS_ThrottleAbs = 4                # Right throttle
THRAXIS_StrafeThrustAmt = 5            # An unused slider is a good choice.

# Set the following actions to the physical switches on the throttle. Switches
# are buttons in the virtual sense, but the logic that uses them assumes they
# can easily be held down indefinitely
SWITCH_CycleFire = 17                  # EFRNORM (Right Fuel Norm Switch)
SWITCH_FlapsDown = 23                  # FLAPD (flaps down)
SWITCH_AutopilotPath = 27              # APALT (Autopilot switch in "PATH")
SWITCH_AutopilotAlt = 28               # APALT (Autopilot switch in "ALT")

# Set the following actions to the physical buttons on the throttle
THRBTN_StrafeRight = 4                 # MSR (thumb hat right)
THRBTN_StrafeLeft = 6                  # MSL (thumb hat left)
THRBTN_StrafeBackward = 2              # MSP (thumb hat press)
THRBTN_AutopilotEngage = 26            # APENG (Autopilot engage)
THRBTN_CycleWeaponAmmo = 11            # CHF (red two way forward)
THRBTN_CycleCounterMeasure = 12        # CHB (red two way backward)

THRHAT_StrafeUpDown = 1                # HAT 1 (up/down)
THRHAT_Roll = 1                        # HAT 1 (left/right)


