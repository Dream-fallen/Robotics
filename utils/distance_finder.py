from vex import *
import config

def drive_until_distance(target_dist_mm, speed=30):
    # Drive forward until the distance sensor hits the target
    # We use a while loop to check the distance sensor constantly
    while config.DISTANCE.distance(MM) > target_dist_mm:
        config.LEFT_MOTOR.spin(FORWARD, speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, speed, PERCENT)
        wait(20, MSEC)
    
    config.LEFT_MOTOR.stop(BRAKE)
    config.RIGHT_MOTOR.stop(BRAKE)

def main():
    config.brain.screen.print("Driving to wall...")
    # Stop when we are 50mm (5cm) away from the wall
    drive_until_distance(50)
    config.brain.screen.print("Wall reached!")

if __name__ == "__main__":
    main()
