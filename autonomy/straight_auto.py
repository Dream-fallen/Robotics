from vex import *
import config

# ---- HARDWARE SETUP ----
brain = Brain()
left_motor = Motor(config.LEFT_MOTOR_PORT, False)  
right_motor = Motor(config.RIGHT_MOTOR_PORT, True) 
inertial = Inertial(config.INERTIAL_PORT) 

def drive_straight_inches(distance_inches, base_speed):
    left_motor.reset_position()
    right_motor.reset_position()
    
    # Pulled conversion values directly from configuration
    target_degrees = (distance_inches / config.WHEEL_CIRCUMFERENCE_INCHES) * 360.0
    
    target_heading = inertial.heading(DEGREES)
    Kp = 1.2  
    
    while True:
        current_left = abs(left_motor.position(DEGREES))
        current_right = abs(right_motor.position(DEGREES))
        average_progress = (current_left + current_right) / 2.0
        
        if average_progress >= target_degrees:
            break
            
        current_heading = inertial.heading(DEGREES)
        error = target_heading - current_heading
        
        while error > 180:  error -= 360
        while error < -180: error += 360
        
        correction = error * Kp
        
        left_speed = max(-100, min(100, base_speed - correction))
        right_speed = max(-100, min(100, base_speed + correction))
        
        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)
        
        wait(20, MSEC)
        
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def main():
    inertial.calibrate()
    while inertial.is_calibrating():
        wait(20, MSEC)
        
    # Drive 24 inches at 40% speed
    drive_straight_inches(24, 40)

if __name__ == "__main__":
    main()
