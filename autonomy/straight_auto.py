from vex import *
import config

# Aliases from config.py
left_motor = config.LEFT_MOTOR
right_motor = config.RIGHT_MOTOR
inertial = config.INERTIAL
brain = config.brain

def drive_straight_inches(distance_inches, base_speed):
    """
    Drives the robot in a straight line for a specific distance.
    Uses the Inertial sensor to maintain a constant heading.
    """
    # 1. Reset encoders to start from 0
    left_motor.reset_position()
    right_motor.reset_position()
    
    # 2. Calculate target degrees
    # Formula: (Distance / Circumference) * 360 degrees per rotation
    # Using config.WHEEL_CIRCUMFERENCE (7.874)
    target_degrees = (distance_inches / config.WHEEL_CIRCUMFERENCE) * 360.0
    
    # 3. Lock in the starting heading
    target_heading = inertial.heading(DEGREES)
    
    # Kp (Proportional Gain): How strongly the robot corrects its path
    # If it wobbles too much, decrease this. If it drifts, increase this.
    Kp = 1.2  
    
    while True:
        # Calculate current distance traveled (Average of both motors)
        current_left = abs(left_motor.position(DEGREES))
        current_right = abs(right_motor.position(DEGREES))
        average_progress = (current_left + current_right) / 2.0
        
        # Exit loop when target distance is reached
        if average_progress >= target_degrees:
            break
            
        # --- HEADING CORRECTION LOGIC ---
        current_heading = inertial.heading(DEGREES)
        error = target_heading - current_heading
        
        # Handle the 0-360 degree wrap-around (The "Compass Problem")
        # Ensures the robot doesn't spin 350 degrees to correct a 10 degree error
        while error > 180:  error -= 360
        while error < -180: error += 360
        
        # Calculate correction value
        correction = error * Kp
        
        # Apply correction to the base speed
        # If drifting right, left motor slows down and right motor speeds up
        l_speed = max(-100, min(100, base_speed - correction))
        r_speed = max(-100, min(100, base_speed + correction))
        
        left_motor.spin(FORWARD, l_speed, PERCENT)
        right_motor.spin(FORWARD, r_speed, PERCENT)
        
        wait(20, MSEC)
        
    # Hard stop to ensure accuracy
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def main():
    brain.screen.clear_screen()
    brain.screen.print("Calibrating Inertial...")
    
    # Calibrate sensor
    inertial.calibrate()
    while inertial.is_calibrating():
        wait(20, MSEC)
        
    brain.screen.print("Driving Straight...")
    
    # Drive 24 inches at 40% speed
    drive_straight_inches(24, 40)
    
    brain.screen.print("Target Reached!")

if __name__ == "__main__":
    main()
