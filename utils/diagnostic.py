from vex import *
import config

# ---- HARDWARE SETUP ----
brain = Brain()

# Adjusted for correct VEX IQ parameters and config structure
left_motor = Motor(config.LEFT_MOTOR_PORT, False)
right_motor = Motor(config.RIGHT_MOTOR_PORT, True)
inertial = Inertial(config.INERTIAL_PORT)

def test_motors():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Testing Motors...")
    
    # Test Left
    left_motor.spin(FORWARD, 20, PERCENT)
    wait(1, SECONDS) # FIXED: Changed SEC to SECONDS
    left_motor.stop()
    
    # Test Right
    right_motor.spin(FORWARD, 20, PERCENT)
    wait(1, SECONDS) # FIXED: Changed SEC to SECONDS
    right_motor.stop()
    
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Motors: OK")

def test_sensors():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Testing Sensors (5s)...")
    
    # FIXED: Replaced global timer with brain.timer
    brain.timer.clear() 
    while brain.timer.time(SECONDS) < 5:
        brain.screen.set_cursor(2, 1)
        # FIXED: Used an f-string to correctly print the dynamic heading value
        brain.screen.print(f"Heading: {inertial.heading():.1f}   ")
        wait(100, MSEC)
    
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Sensors: OK")

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("--- ROBOT DIAGNOSTICS ---")
    wait(1, SECONDS) # FIXED: Changed SEC to SECONDS
    
    # 1. Run Motor Test
    test_motors()
    wait(1, SECONDS) # FIXED: Changed SEC to SECONDS
    
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
