from vex import *

# ---- HARDWARE SETUP ----
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 
inertial = Inertial(Ports.PORT10) 

def turn_to_angle(target_angle):
    # Simple Proportional Control (P-Loop)
    Kp = 2.0 # Tuning constant: increase if too slow, decrease if it overshoots
    
    while True:
        current_angle = inertial.heading()
        error = target_angle - current_angle
        
        if abs(error) < 2: # Stop when within 2 degrees of target
            break
            
        speed = error * Kp
        speed = max(min(speed, 50), -50) # Cap speed at 50%
        
        left_motor.spin(FORWARD, speed, PERCENT)
        right_motor.spin(FORWARD, -speed, PERCENT)
        wait(20, MSEC)
    
    left_motor.stop()
    right_motor.stop()

def main():
    inertial.calibrate()
    while inertial.isCalibrating():
        wait(20, MSEC)
        
    # Example: Turn to 90 degrees
    turn_to_angle(90)

main()
