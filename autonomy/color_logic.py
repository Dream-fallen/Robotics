from vex import *
import config

def drive_until_color(target_color, speed=30):
    """Drives forward until the Optical sensor detects the target color"""
    config.brain.screen.print(f"Searching for {target_color}...")
    
    while True:
        if config.OPTICAL.color() == target_color:
            break
        
        config.LEFT_MOTOR.spin(FORWARD, speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, speed, PERCENT)
        wait(20, MSEC)
    
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)
    config.brain.screen.print("Color Found!")

def main():
    # Example: Drive until we see a RED object, then stop
    drive_until_color(Color.RED)
