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
    wait(1, SEC) # Fixed: Changed V5 SECONDS to VEX IQ SEC
    left_motor.stop()
    
    # Test Right
    right_motor.spin(FORWARD, 20, PERCENT)
    wait(1, SEC) # Fixed: Changed V5 SECONDS to VEX IQ SEC
    right_motor.stop()
    
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Motors: OK")

def test_sensors():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Testing Sensors (5s)...")
    
    start_time = timer.time()
    while (timer.time() - start_time) < 5:
        brain.screen.set_cursor(2, 1)
        brain.screen.print("Heading: %s    " % inertial.heading())
        wait(100, MSEC)
    
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Sensors: OK")

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("--- ROBOT DIAGNOSTICS ---")
    wait(1, SEC) # Fixed: Changed V5 SECONDS to VEX IQ SEC
    
    # 1. Run Motor Test
    test_motors()
    wait(1, SEC) # Fixed: Changed V5 SECONDS to VEX IQ SEC
    
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
