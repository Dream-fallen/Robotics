from vex import *
import config

# ---- HARDWARE SETUP ----
# We do NOT declare Motor() or Brain() here. 
# We use the objects already created in config.py.
brain = config.brain
left_motor = config.LEFT_MOTOR
right_motor = config.RIGHT_MOTOR
inertial = config.INERTIAL

def test_motors():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Testing Motors...")
    
    # Test Left
    # Use .spin(FORWARD, velocity, PERCENT)
    left_motor.spin(FORWARD, 20, PERCENT)
    wait(1, SECONDS) 
    left_motor.stop()
    
    wait(0.5, SECONDS) # Small gap between tests
    
    # Test Right
    right_motor.spin(FORWARD, 20, PERCENT)
    wait(1, SECONDS) 
    right_motor.stop()
    
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Motors: OK")

def test_sensors():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Testing Sensors (5s)...")
    
    # The brain timer is used to track the 5-second window
    brain.timer.clear() 
    while brain.timer.time(SECONDS) < 5:
        brain.screen.set_cursor(2, 1)
        # Reference the inertial sensor from config
        # heading() returns the current angle of the robot
        brain.screen.print(f"Heading: {inertial.heading():.1f}   ")
        wait(100, MSEC)
    
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Sensors: OK")

def main():
    # Clear screen and show header
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("--- ROBOT DIAGNOSTICS ---")
    wait(1, SECONDS) 
    
    # 1. Run Motor Test
    test_motors()
    wait(1, SECONDS) 
    
    # 2. Run Sensor Test
    test_sensors()
    
    # Final Summary
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Diagnostics Complete!")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Check Brain for errors.")

if __name__ == "__main__":
    main()
