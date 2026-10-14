from vex import *

# ---- HARDWARE SETUP ----
brain = Brain()
# VEX IQ ports use integer numbers 1-12
left_motor = Motor(Ports.PORT1, False)  
right_motor = Motor(Ports.PORT6, True) 
inertial = Inertial(Ports.PORT10) 

# ---- CONSTANTS ----
WHEEL_CIRCUMFERENCE_INCHES = 7.874  # Standard VEX IQ 200mm tires

def drive_straight_inches(distance_inches, base_speed):
    # 1. Reset motor encoder positions before starting
    left_motor.reset_position()
    right_motor.reset_position()
    
    # 2. Calculate target encoder steps (degrees of rotation)
    # Total Rotations = Distance / Wheel Circumference
    # Total Degrees = Total Rotations * 360
    target_degrees = (distance_inches / WHEEL_CIRCUMFERENCE_INCHES) * 360.0
    
    # 3. Lock onto our straight-line target heading
    target_heading = inertial.heading(DEGREES)
    Kp = 1.2  # Heading correction aggressiveness (Tune this: 0.8 to 1.5)
    
    # Loop runs until the average distance of both wheels hits the target
    while True:
        # Calculate current progress via motor encoders
        current_left = abs(left_motor.position(DEGREES))
        current_right = abs(right_motor.position(DEGREES))
        average_progress = (current_left + current_right) / 2.0
        
        # Exit condition: Stop loop once distance is achieved
        if average_progress >= target_degrees:
            break
            
        # 4. Heading error calculation (with VEX IQ 0-360 wrap-around fix)
        current_heading = inertial.heading(DEGREES)
        error = target_heading - current_heading
        
        while error > 180:  error -= 360
        while error < -180: error += 360
        
        correction = error * Kp
        
        # 5. Apply velocities balanced within constraints
        left_speed = max(-100, min(100, base_speed - correction))
        right_speed = max(-100, min(100, base_speed + correction))
        
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)
        
        wait(20, MSEC)
        
    # 6. Force a solid stop at the destination
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def main():
    # VEX IQ snake_case method for checking calibration
    inertial.calibrate()
    while inertial.is_calibrating():
        wait(20, MSEC)
        
    # Example: Drive exactly 24 inches at 40% speed
    drive_straight_inches(24, 40)

main()
