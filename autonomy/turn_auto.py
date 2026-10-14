from vex import *
import config

# ---- HARDWARE SETUP ----
brain = Brain()
left_motor = Motor(config.LEFT_MOTOR_PORT, False)
right_motor = Motor(config.RIGHT_MOTOR_PORT, True) 
inertial = Inertial(config.INERTIAL_PORT) 

def turn_to_angle(target_angle):
    Kp = 1.5 
    inertial.set_rotation(0, DEGREES) 
    
    while True:
        current_angle = inertial.rotation(DEGREES)
        error = target_angle - current_angle
        
        if abs(error) < 1.5: 
            break
            
        speed = error * Kp
        
        if speed > 50: speed = 50
        elif speed < -50: speed = -50
        
        left_motor.spin(FORWARD, speed, PERCENT)
        right_motor.spin(FORWARD, -speed, PERCENT)
        wait(20, MSEC)
    
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def main():
    inertial.calibrate()
    while inertial.is_calibrating():
        wait(20, MSEC)
    wait(500, MSEC) 
        
    # Turn 90 degrees to the right
    turn_to_angle(90)

if __name__ == "__main__":
    main()
