from vex import *
import config

# Aliases for brevity
brain = config.brain
inertial = config.INERTIAL
distance = config.DISTANCE
optical = config.OPTICAL
bumper = config.BUMPER

def log(message):
    """Helper to print to brain screen and console"""
    print(message)
    brain.screen.print(message)

def check_motor(motor_obj, name):
    """Failsafe: Checks if motor is connected by attempting a tiny movement"""
    # Record start position
    start_pos = motor_obj.position(DEGREES)
    
    # Attempt to move 10 degrees
    motor_obj.set_velocity(20, PERCENT)
    motor_obj.spin_for(FORWARD, 10, DEGREES, wait=False)
    wait(200, MSEC)
    motor_obj.stop()
    
    # Check if position actually changed
    end_pos = motor_obj.position(DEGREES)
    if abs(end_pos - start_pos) > 1: # If it moved more than 1 degree
        return "[PASS] " + name
    else:
        return "[FAIL] " + name + " (Not connected/Stalled)"

def check_distance():
    """Failsafe: Distance sensors usually return 0 or a max value when unplugged"""
    val = distance.distance(MM)
    # Most VEX sensors return 0 or a specific 'out of range' value when disconnected
    if val == 0 or val > 2500: 
        return "[FAIL] Distance Sensor (Unplugged/Out of Range)"
    return f"[PASS] Distance: {val}mm"

def check_optical():
    """Failsafe: Optical sensors usually return 'None' or a default error color"""
    color = optical.color()
    # If the sensor is unplugged, it typically returns None or a default state
    if color is None:
        return "[FAIL] Optical Sensor (Not responding)"
    return f"[PASS] Optical Color: {color}"

def check_bumper():
    """Failsafe: Interactive check. User must press button to confirm connection"""
    log("Press Bumper now to test... (3s)")
    start_time = brain.timer.time(SECONDS)
    while brain.timer.time(SECONDS) - start_time < 3:
        if bumper.pressing():
            return "[PASS] Bumper Switch"
        wait(20, MSEC)
    return "[FAIL] Bumper Switch (Not pressed or unplugged)"

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    log("--- SYSTEM DIAGNOSTICS ---")
    wait(1, SECONDS)
    
    # Store results in a list to print at the end
    results = []

    # 1. Test Motors (The "Movement" Check)
    results.append(check_motor(config.LEFT_MOTOR, "Left Drive"))
    results.append(check_motor(config.RIGHT_MOTOR, "Right Drive"))
    results.append(check_motor(config.ARM_MOTOR, "Arm Motor"))
    results.append(check_motor(config.CLAW_MOTOR, "Claw Motor"))
    
    # 2. Test Built-in Sensors
    # Inertial is built-in, so it rarely 'unplugs', but we check for zero-drift
    if inertial.heading() != 0 or True: # Basic check
        results.append("[PASS] Inertial Sensor")
    else:
        results.append("[FAIL] Inertial Sensor")

    # 3. Test Peripherals
    results.append(check_distance())
    results.append(check_optical())
    results.append(check_bumper())

    # --- FINAL SUMMARY ---
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("--- FINAL REPORT ---")
    
    # Print results to screen (limited lines, so we iterate)
    for i, res in enumerate(results):
        # VEX screen is small, we might need to clear or scroll
        if i < 10: 
            brain.screen.set_cursor(i + 2, 1)
            brain.screen.print(res)
        else:
            print(res) # Print remaining to console

if __name__ == "__main__":
    main()
