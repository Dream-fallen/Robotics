from vex import *
import config

def handle_driver_control():
    # Use a variable to keep track of which mode we are in
    # 0 = Arcade, 1 = Tank
    drive_mode = 0 
    controller = Controller()

    while True:
        # Toggle mode with Button L1
        if controller.buttonL1.pressing():
            drive_mode = 1 if drive_mode == 0 else 0
            wait(200, MSEC) # Debounce

        if drive_mode == 0: # Arcade
            forward = controller.axis3.position()
            turn = controller.axis4.position()
            if abs(forward) < config.DEADBAND: forward = 0
            if abs(turn) < config.DEADBAND: turn = 0
            
            config.LEFT_MOTOR.spin(FORWARD, max(-100, min(100, forward + turn)), PERCENT)
            config.RIGHT_MOTOR.spin(FORWARD, max(-100, min(100, forward - turn)), PERCENT)
        
        else: # Tank
            left = controller.axis3.position()
            right = controller.axis2.position()
            if abs(left) < config.DEADBAND: left = 0
            if abs(right) < config.DEADBAND: right = 0
            
            config.LEFT_MOTOR.spin(FORWARD, left, PERCENT)
            config.RIGHT_MOTOR.spin(FORWARD, right, PERCENT)
            
        wait(20, MSEC)
