from vex import *
import config

# Define named positions (Absolute degrees from the 0 point)
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
        # Set velocity first
        config.ARM_MOTOR.set_velocity(speed, PERCENT)
        # FIXED: Changed spin_for to spin_to_position for absolute movement
        config.ARM_MOTOR.spin_to_position(target, DEGREES)
    else:
        print("Invalid Arm Position")

def move_claw(position_name, speed=50):
    if position_name in CLAW_POSITIONS:
        target = CLAW_POSITIONS[position_name]
        # Set velocity first
        config.CLAW_MOTOR.set_velocity(speed, PERCENT)
        # FIXED: Changed spin_for to spin_to_position for absolute movement
        config.CLAW_MOTOR.spin_to_position(target, DEGREES)
    else:
        print("Invalid Claw Position")
