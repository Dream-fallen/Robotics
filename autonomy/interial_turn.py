from vex import *

# ---- HARDWARE SETUP ----
brain = Brain()
# FIX: Removed the 'GearSetting.RATIO_18_1' strings which caused compiler errors on IQ
left_motor = Motor(Ports.PORT1, False)
right_motor = Motor(Ports.PORT6, True) 
inertial = Inertial(Ports.PORT10) 

def turn_to_angle(target_angle):
    # Simple Proportional Control (P-Loop)
    Kp = 1.5 
    
    # Reset rotation to 0 before the turn so target_angle is relative to current facing
    inertial.set_rotation(0, DEGREES) 
    
    while True:
        # Using rotation() safely avoids the 0-360 wrap-around glitch
        current_angle = inertial.rotation(DEGREES)
        error = target_angle - current_angle
        
        # Stop when within 1.5 degrees of target
        if abs(error) < 1.5: 
            break
            
        speed = error * Kp
        
        # Clean speed cap matching direction
        if speed > 50: speed = 50
        elif speed < -50: speed = -50
        
        left_motor.spin(FORWARD, speed, PERCENT)
        right_motor.spin(FORWARD, -speed, PERCENT)
        wait(20, MSEC)
    
    # Explicitly hold position or brake
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def main():
    # Calibrate with ample time given to sit still
    inertial.calibrate()
    while inertial.is_calibrating():
        wait(20, MSEC)
    wait(500, MSEC) # Extra safety buffer after calibration ends
        
    # Example: Turn 90 degrees to the right
    turn_to_angle(90)

main()
