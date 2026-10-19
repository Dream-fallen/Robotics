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
        # Set velocity first using PERCENT unit
        config.ARM_MOTOR.set_velocity(speed, PERCENT)
        # Spin to target; by default spin_for blocks execution until done
        config.ARM_MOTOR.spin_for(FORWARD, target, DEGREES)
    else:
        print("Invalid Arm Position")

def move_claw(position_name, speed=50):
    if position_name in CLAW_POSITIONS:
        target = CLAW_POSITIONS[position_name]
        # Set velocity first using PERCENT unit
        config.CLAW_MOTOR.set_velocity(speed, PERCENT)
        # Spin to target; by default spin_for blocks execution until done
        config.CLAW_MOTOR.spin_for(FORWARD, target, DEGREES)
    else:
        print("Invalid Claw Position")
