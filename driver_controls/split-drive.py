from vex import *
import config

# Aliases for cleaner code
left_motor = config.LEFT_MOTOR
right_motor = config.RIGHT_MOTOR
controller = config.controller
brain = config.brain

# Constants
DEADBAND = config.DEADBAND 

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Mode: Split-Stick Drive")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("L-Stick: Throttle | R-Stick: Turn")

    while True:
        # 1. Read Joystick Values
        # axisA is Left Vertical (Forward/Backward)
        # axisC is Right Horizontal (Left/Right)
        throttle = controller.axisA.position() 
        turn = controller.axisC.position()     
        
        # 2. Apply Deadband
        # This stops the robot from creeping if the sticks are slightly worn
        if abs(throttle) < DEADBAND: 
            throttle = 0
        if abs(turn) < DEADBAND: 
            turn = 0

        # 3. Mix Channels
        # Throttle moves both motors in the same direction
        # Turn moves motors in opposite directions
        left_speed = throttle + turn
        right_speed = throttle - turn

        # 4. Clamp Values
        # Ensures we never send more than 100% or less than -100%
        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)

        # 5. Apply to Motors
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        # Prevent CPU hogging
        wait(20, MSEC)

if __name__ == "__main__":
    main()
