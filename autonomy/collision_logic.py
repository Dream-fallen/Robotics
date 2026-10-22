from vex import *
import config

def safe_drive_straight(distance_inches, speed=40):
    """Drives straight, but STOPS immediately if the bumper is pressed"""
    target_degrees = (distance_inches / config.WHEEL_CIRCUMFERENCE) * 360.0
    config.LEFT_MOTOR.reset_position()
    config.RIGHT_MOTOR.reset_position()
    
    while True:
        # FAILSAFE: Check bumper every single loop
        if config.BUMPER.pressing():
            config.brain.screen.print("COLLISION DETECTED!")
            break
            
        avg_pos = (abs(config.LEFT_MOTOR.position(DEGREES)) + abs(config.RIGHT_MOTOR.position(DEGREES))) / 2
        if avg_pos >= target_degrees:
            break
            
        config.LEFT_MOTOR.spin(FORWARD, speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, speed, PERCENT)
        wait(20, MSEC)
        
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)
