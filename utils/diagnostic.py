from vex import *
import config # Importing the config file we created earlier

# ---- HARDWARE SETUP ----
brain = Brain()
# Initialize hardware using the constants from config.py
left_motor = Motor(config.LEFT_MOTOR_PORT, config.GEAR_RATIO, False)
right_motor = Motor(config.RIGHT_MOTOR_PORT, config.GEAR_RATIO, True)
inertial = Inertial(config.INERTIAL_PORT)

def test_motors():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Testing Motors...")
    
    # Test Left
    left_motor.spin(FORWARD, 20, PERCENT)
    wait(1, SECONDS)
    left_motor.stop()
    
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
    
    # Run the sensor read for 5 seconds instead of an infinite loop
    start_time = timer.time()
    while (timer.time() - start_time) < 5:
        brain.screen.set_cursor(2, 1)
        # Clear the line by printing spaces, then print new value
        brain.screen.print("Heading: %s    " % inertial.heading())
        wait(100, MSEC)
    
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Sensors: OK")

def main():
    """
    Orchestrates the diagnostic sequence.
    """
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

# Properly call the main function to start the script
if __name__ == "__main__":
    main()
