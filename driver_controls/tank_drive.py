# Tank Drive requires 2 motors. Left Joystick controls the Left Motor. Right Joystick controls the Right Motor.

from vex import *

# ---- HARDWARE SETUP ----
brain = Brain()
controller = Controller()

# Setup Motors (Change ports and direction configuration to match your robot)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 

def main():
    brain.screen.print("Tank Drive Active")

    while True:
        # Read the vertical position of both joysticks
        left_speed = controller.axis3.position()   # Left Stick Up/Down
        right_speed = controller.axis2.position()  # Right Stick Up/Down

        # Apply speeds to motors
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        # Allow the brain's processor to rest briefly
        wait(20, MSEC)

main()
