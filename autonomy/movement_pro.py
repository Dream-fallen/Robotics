from vex import *
import config

def turn_to_angle(target_angle, speed=40):
    Kp = 1.5
    config.INERTIAL.set_rotation(0, DEGREES) 
    
    while True:
        error = target_angle - config.INERTIAL.rotation(DEGREES)
        if abs(error) < 1.5: break
        
        move_speed = max(-speed, min(speed, error * Kp))
        config.LEFT_MOTOR.spin(FORWARD, move_speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, -move_speed, PERCENT)
        wait(20, MSEC)
    
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)

def drive_straight(distance_inches, base_speed=40):
    target_degrees = (distance_inches / config.WHEEL_CIRCUMFERENCE) * 360.0
    config.LEFT_MOTOR.reset_position()
    config.RIGHT_MOTOR.reset_position()
    target_heading = config.INERTIAL.heading(DEGREES)
    Kp = 1.2
    
    while True:
        avg_pos = (abs(config.LEFT_MOTOR.position(DEGREES)) + abs(config.RIGHT_MOTOR.position(DEGREES))) / 2
        if avg_pos >= target_degrees: break
        
        error = target_heading - config.INERTIAL.heading(DEGREES)
        while error > 180: error -= 360
        while error < -180: error += 360
        
        correction = error * Kp
        config.LEFT_MOTOR.spin(FORWARD, max(-100, min(100, base_speed - correction)), PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, max(-100, min(100, base_speed + correction)), PERCENT)
        wait(20, MSEC)
        
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)
