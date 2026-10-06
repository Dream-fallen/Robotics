# Arcade Drive only requires one motor, and thus only one control stick. Axis 3 = Forward, Axis 4 = Turn.

from vex import *

# ---- HARDWARE SETUP ----
brain = Brain()
controller = Controller()

# Setup Motors (Change ports and direction configuration to match your robot)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 

def main():
    brain.screen.print("Arcade Drive Active")

    while True:
        # Read forward/backward power and turning power from the left joystick
        forward_power = controller.axis3.position()  # Left Stick Up/Down
        turn_power = controller.axis4.position()     # Left Stick Left/Right
        
        # Mix the channels to calculate individual motor speeds
        left_speed = forward_power + turn_power
        right_speed = forward_power - turn_power

        # Apply speeds to motors
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        # Allow the brain's processor to rest briefly
        wait(20, MSEC)

main()
