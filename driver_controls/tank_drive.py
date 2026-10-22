from vex import *
import config

# Aliases for cleaner code - Use the hardware already created in config.py
left_motor = config.LEFT_MOTOR
right_motor = config.RIGHT_MOTOR
controller = config.controller
brain = config.brain

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Mode: Tank Drive")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("L-Stick: Left | R-Stick: Right")

    while True:
        # 1. Read Joystick Values
        # axisA is Left Vertical (Controls Left Motor)
        # axisD is Right Vertical (Controls Right Motor)
        left_speed = controller.axisA.position()
        right_speed = controller.axisD.position()

        # 2. Apply DEADBAND from config.py
        # Prevents the robot from drifting if sticks don't center perfectly
        if abs(left_speed) < config.DEADBAND: 
            left_speed = 0
        if abs(right_speed) < config.DEADBAND: 
            right_speed = 0

        # 3. Apply to Motors
        # Because the motors are already defined as FORWARD/REVERSE in config.py,
        # we just need to send the power.
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        # Prevent CPU hogging
        wait(20, MSEC)

if __name__ == "__main__":
    main()
