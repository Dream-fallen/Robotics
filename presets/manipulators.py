from vex import *
import config

# Define named positions (Tune these numbers for the actual build!)
ARM_POSITIONS = {
    "IDLE": 0,
    "PICKUP": 450,
    "SCORE": 900
}

CLAW_POSITIONS = {
    "OPEN": 0,
    "CLOSED": 120
}

def move_arm(position_name, speed=50):
    if position_name in ARM_POSITIONS:
        target = ARM_POSITIONS[position_name]
        config.ARM_MOTOR.spin_for(FORWARD, target, DEGREES, speed, wait=True)
    else:
        print("Invalid Arm Position")

def move_claw(position_name, speed=50):
    if position_name in CLAW_POSITIONS:
        target = CLAW_POSITIONS[position_name]
        config.CLAW_MOTOR.spin_for(FORWARD, target, DEGREES, speed, wait=True)
    else:
        print("Invalid Claw Position")
