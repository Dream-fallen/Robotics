from vex import *

# ---- HARDWARE SETUP ----
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 
inertial = Inertial(Ports.PORT10) 

def drive_straight(distance_inches, speed_percent):
    # This is a simplified PID (just the P) for heading correction
    target_heading = inertial.heading()
    Kp = 1.5 # Correction strength
    
    # Roughly calculate time based on speed (this varies by robot)
    # For a professional repo, you'd use encoders here.
    drive_time = (distance_inches * 0.1) / (speed_percent / 100) 
    
    start_time = timer.time()
    while (timer.time() - start_time) < drive_time:
        # Calculate error from the starting heading
        error = target_heading - inertial.heading()
        correction = error * Kp
        
        # Apply correction to keep the robot straight
        left_motor.spin(FORWARD, speed_percent - correction, PERCENT)
        right_motor.spin(FORWARD, speed_percent + correction, PERCENT)
        
        wait(20, MSEC)
    
    left_motor.stop()
    right_motor.stop()

def main():
    inertial.calibrate()
    while inertial.isCalibrating():
        wait(20, MSEC)
        
    # Drive straight for 24 inches at 40% power
    drive_straight(24, 40)

main()
