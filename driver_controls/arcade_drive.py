from vex import *
import config

# Aliases for cleaner code
left_motor = config.LEFT_MOTOR
right_motor = config.RIGHT_MOTOR
controller = config.controller
brain = config.brain

# Constants
DEADBAND = config.DEADBAND  # Use the 10 defined in config.py

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Mode: Arcade Drive")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Stick: Left (A=Fwd, B=Turn)")

    while True:
        # 1. Read Joystick Values
        # axisA is Vertical (Throttle), axisB is Horizontal (Turn)
        forward = controller.axisA.position() 
        turn = controller.axisB.position()     
        
        # 2. Apply Deadband
        # Prevents the robot from "humming" or drifting when the stick is centered
        if abs(forward) < DEADBAND: 
            forward = 0
        if abs(turn) < DEADBAND: 
            turn = 0

        # 3. Mix Channels (The Arcade Drive Formula)
        # Left = Forward + Turn
        # Right = Forward - Turn
        left_speed = forward + turn
        right_speed = forward - turn

        # 4. Clamp Values
        # Ensure values stay between -100 and 100 to prevent API errors
        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)

        # 5. Apply to Motors
        # We use the motor objects from config.py
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        # Prevent CPU hogging
        wait(20, MSEC)

if __name__ == "__main__":
    main()
