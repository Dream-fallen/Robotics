from vex import *
import config

def drive_until_distance(target_mm, speed=30):
    """Drives forward until the distance sensor sees an object."""
    while config.DISTANCE.distance(MM) > target_mm:
        config.LEFT_MOTOR.spin(FORWARD, speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, speed, PERCENT)
        wait(20, MSEC)
    
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)

def drive_until_color(target_color, speed=30):
    """Drives forward until the optical sensor detects a specific color."""
    # target_color should be something like Color.RED
    while config.OPTICAL.color() != target_color:
        config.LEFT_MOTOR.spin(FORWARD, speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, speed, PERCENT)
        wait(20, MSEC)
        
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)
