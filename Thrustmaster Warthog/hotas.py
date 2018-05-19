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
RUDDER_PEDALS_INVERT = -1.0 # must be -1.0 or 1.0 (negative for invert)

##############################################################################
# Rudder Pedals Information
RUD_Name = "Mad Catz Pro Flight Combat Rudder Pedals"
RUD_Id = 111347556

# Set the following actions to the physical axes on your rudder. 
RUDAXIS_Reverse = 1
RUDAXIS_Boost = 2
RUDAXIS_Roll = 3

RUDAXISBTN_Threshold = -0.5         # Less than = no press

##############################################################################
# Joystick Information
JOY_Name = "Joystick - HOTAS Warthog"
JOY_Id = 72287234

# Set desired offset rotation amount in degrees. This is useful for those who
# have a centered joystick that are mounted in this way for ergonomic reasons
JOY_Rotation = -39

# Set the following actions to the physical axes on the joystick
JOYAXIS_Yaw = 1
JOYAXIS_Pitch = 2

# Set the following actions to the physical buttons on the joystick
JOYBTN_FireWep = 1                     # TG1 (Trigger stage 1)
JOYBTN_FocusFireZoom = 6               # TG2 (Trigger stage 2)
JOYBTN_CycleWepGrp = 3                 # S3 (pinky button)
JOYBTN_Missiles = 2                    # S2 (red button)
JOYBTN_CycleWeaponAmmo = 5             # S1 (index finger button)

# (optional mod-lever held)
SWITCH_JoystickAltMod = 4              # S4 (mod-lever in back)

JOYBTN_ShieldFront_Top = 7             # H2U
JOYBTN_ShieldBack_Bottom = 9           # H2D
JOYBTN_ShieldLeft = 8                  # H2R
JOYBTN_ShieldRight = 10                # H2L

JOYBTN_ResetPowerDistribution = 11     # H3U
JOYBTN_IncPower1 = 14                  # H3L
JOYBTN_IncPower2 = 12                  # H3R
JOYBTN_IncPower3 = 13                  # H3D

JOYBTN_TgtReticle_CycleAll = 15        # H4U 
JOYBTN_TgtCyclePin_SetPin = 19         # H4P
JOYBTN_TgtNearestEnemy_CycleAllBck = 17# H4D
JOYBTN_TgtEnemyFwd_FriendlyFwd = 16    # H4R
JOYBTN_TgtEnemyBck_FriendlyBck = 18    # H4L

JOYHAT_Zoom = 1

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
SWITCH_FlapsUp = 22                    # FLAPU (flaps up)
SWITCH_FlapsDown = 23                  # FLAPD (flaps down)
SWITCH_AutopilotPath = 27              # APALT (Autopilot switch in "PATH")
SWITCH_AutopilotAlt = 28               # APALT (Autopilot switch in "ALT")
SWITCH_ModeOnFoot = 13                 # PSF (Pinky switch forward)
SWITCH_ModeVehicle = 14                # PSB (Pinky switch backward)
SWITCH_Power = 20                      # APU ON

# Set the following actions to the physical buttons on the throttle
THRBTN_StrafeUp = 3                    # MSU (thumb hat up)
THRBTN_StrafeDown = 5                  # MSD (thumb hat down)
THRBTN_StrafeRight = 4                 # MSR (thumb hat right)
THRBTN_StrafeLeft = 6                  # MSL (thumb hat left)
THRBTN_ResetZoom = 2                   # MSP (thumb hat press)
THRBTN_AutopilotEngage = 26            # APENG (Autopilot engage)
THRBTN_CycleCounterMeasure = 11        # CHF (red two way forward)
THRBTN_LaunchCounterMeasures = 12      # CHB (red two way backward)
THRBTN_LandingGear = 21                # LDGH (Landing Gear button)
THRBTN_Afterburner = 7                 # SPDF (Fat two way forward) (locks)
THRBTN_LookBehind = 8                  # SPDB (Fat two way backward)
THRBTN_DecoupledModeToggle = 15        # LTB (red pinky button)

#THRBTN_ShieldRaise = 31                # IGNON L
THRBTN_FlightReadyToggle = 32                # IGNON R

#THRBTN_IncreaseCoolerRate
#THRBTN_DecreaseCoolerRate
#THRBTN_FlightSystemsReady
#THRBTN_OpenAllDoors
#THRBTN_CloseAllDoors
#THRBTN_LockAllDoors
#THRBTN_UnlockAllDoors

THRHAT_StrafeUpDown = 1                # HAT 1 (up/down)
THRHAT_Roll = 1                        # HAT 1 (left/right)


