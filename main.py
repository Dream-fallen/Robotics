from vex import *
import config
import manipulators
import sensor_utils
import movement_pro
import input_manager

def autonomous():
    # 1. Calibrate Inertial
    config.INERTIAL.calibrate()
    while config.INERTIAL.is_calibrating():
        wait(20, MSEC)
        
    # 2. Run a sequence of professional movements
    movement_pro.drive_straight(24, 40)     # Drive 24 inches
    movement_pro.turn_to_angle(90)          # Turn 90 degrees
    sensor_utils.drive_until_distance(100)  # Drive until 100mm from wall
    
    # 3. Use the manipulator
    manipulators.move_claw("CLOSED")
    manipulators.move_arm("SCORE")
    manipulators.move_claw("OPEN")
    manipulators.move_arm("IDLE")

def main():
    # Start Autonomous
    autonomous()
    
    # Then enter Driver Control
    input_manager.handle_driver_control()

if __name__ == "__main__":
    main()
