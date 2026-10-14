from vex import *
import config

# ---- HARDWARE SETUP ----
left_motor = Motor(config.LEFT_MOTOR_PORT, False)
right_motor = Motor(config.RIGHT_MOTOR_PORT, True) 

def main():
    # Drive forward for 2 seconds
    left_motor.spin(FORWARD, 50, PERCENT)
    right_motor.spin(FORWARD, 50, PERCENT)
    wait(2, SEC) 
    
    # Stop
    left_motor.stop()
    right_motor.stop()
    wait(0.5, SEC) 
    
    # Turn right for 1 second
    left_motor.spin(FORWARD, 40, PERCENT)
    right_motor.spin(REVERSE, 40, PERCENT)
    wait(1, SEC) 
    
    left_motor.stop()
    right_motor.stop()

if __name__ == "__main__":
    main()
