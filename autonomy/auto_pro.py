from vex import *
import config

# ---- ARM/CLAW PRESETS ----
ARM_POSITIONS = {"IDLE": 0, "PICKUP": 450, "SCORE": 900}
CLAW_POSITIONS = {"OPEN": 0, "CLOSED": 120}

def move_arm(position_name, speed=50):
    if position_name in ARM_POSITIONS:
        target = ARM_POSITIONS[position_name]
        config.ARM_MOTOR.set_velocity(speed, PERCENT)
        config.ARM_MOTOR.spin_to_position(target, DEGREES)

def move_claw(position_name, speed=50):
    if position_name in CLAW_POSITIONS:
        target = CLAW_POSITIONS[position_name]
        config.CLAW_MOTOR.set_velocity(speed, PERCENT)
        config.CLAW_MOTOR.spin_to_position(target, DEGREES)

# ---- NAVIGATION FUNCTIONS ----

def turn_to_angle(target_angle, speed=40):
    """Turns robot to a specific relative angle (Positive=Right, Negative=Left)"""
    Kp = 1.5
    config.INERTIAL.reset() # Reset relative rotation to 0
    
    while True:
        error = target_angle - config.INERTIAL.rotation(DEGREES)
        if abs(error) < 1.5: break
        
        move_speed = max(-speed, min(speed, error * Kp))
        config.LEFT_MOTOR.spin(FORWARD, move_speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, -move_speed, PERCENT)
        wait(20, MSEC)
    
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)

def drive_straight(distance_inches, base_speed=40):
    """Drives straight for X inches using Inertial correction"""
    target_degrees = (distance_inches / config.WHEEL_CIRCUMFERENCE) * 360.0
    config.LEFT_MOTOR.reset_position()
    config.RIGHT_MOTOR.reset_position()
    target_heading = config.INERTIAL.heading(DEGREES)
    Kp = 1.2
    
    while True:
        avg_pos = (abs(config.LEFT_MOTOR.position(DEGREES)) + abs(config.RIGHT_MOTOR.position(DEGREES))) / 2
        if avg_pos >= target_degrees: break
        
        error = target_heading - config.INERTIAL.heading(DEGREES)
        while error > 180: error -= 360
        while error < -180: error += 360
        
        correction = error * Kp
        config.LEFT_MOTOR.spin(FORWARD, max(-100, min(100, base_speed - correction)), PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, max(-100, min(100, base_speed + correction)), PERCENT)
        wait(20, MSEC)
        
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)

# ---- MISSION SEQUENCE ----

def main():
    # 1. Initialization
    config.brain.screen.clear_screen()
    config.brain.screen.print("Calibrating...")
    config.INERTIAL.calibrate()
    while config.INERTIAL.is_calibrating():
        wait(20, MSEC)
    
    # 2. The Mission Script
    # You can now write your autonomous path like a story:
    
    # Step 1: Drive forward to the object
    drive_straight(24, 40)
    wait(200, MSEC)
    
    # Step 2: Lower arm and close claw
    move_arm("PICKUP")
    move_claw("CLOSED")
    wait(500, MSEC)
    
    # Step 3: Lift arm to scoring height
    move_arm("SCORE")
    
    # Step 4: Turn 90 degrees right to the scoring zone
    turn_to_angle(90)
    wait(200, MSEC)
    
    # Step 5: Drive forward into the zone
    drive_straight(12, 30)
    
    # Step 6: Open claw to release object
    move_claw("OPEN")
    
    config.brain.screen.print("Mission Complete!")

if __name__ == "__main__":
    main()
