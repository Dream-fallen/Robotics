from vex import *
import config

# Aliases from config.py
left_motor = config.LEFT_MOTOR
right_motor = config.RIGHT_MOTOR
inertial = config.INERTIAL
brain = config.brain

def turn_to_angle(target_angle):
    """
    Turns the robot to a specific angle using a P-Loop.
    target_angle: Degrees to turn (Positive = Right, Negative = Left)
    """
    # Kp (Proportional Gain) determines how aggressively the robot turns
    # If it oscillates (wobbles), lower this. If it's too slow, raise it.
    Kp = 1.5 
    
    # Reset the rotation sensor to 0 before starting the turn
    inertial.reset() 
    
    while True:
        # Get the current rotation (relative to the reset point)
        current_angle = inertial.rotation(DEGREES)
        error = target_angle - current_angle
        
        # Stop when we are within 1.5 degrees of the target (Tolerance)
        if abs(error) < 1.5: 
            break
            
        # Calculate speed based on error (Further away = faster)
        speed = error * Kp
        
        # Clamp speed to avoid wheel slip (Max 50%, Min -50%)
        if speed > 50: speed = 50
        elif speed < -50: speed = -50
        
        # For a turn: Left motor and Right motor must spin in opposite directions
        left_motor.spin(FORWARD, speed, PERCENT)
        right_motor.spin(FORWARD, -speed, PERCENT)
        
        wait(20, MSEC)
    
    # Hard stop to prevent drifting
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def main():
    brain.screen.clear_screen()
    brain.screen.print("Calibrating Inertial...")
    
    # 1. Calibrate the built-in Inertial Sensor
    # IMPORTANT: Robot must be perfectly still during this!
    inertial.calibrate()
    
    # Wait for calibration to complete
    while inertial.is_calibrating():
        wait(20, MSEC)
    
    brain.screen.print("Calibrated. Turning...")
    wait(500, MSEC) 
        
    # 2. Execute Turn
    # Turn 90 degrees to the right
    turn_to_angle(90)
    
    brain.screen.print("Turn Complete!")

if __name__ == "__main__":
    main()
