from vex import *
import config

# ---- HARDWARE SETUP ----
brain = Brain()
controller = Controller()

# Fixed VEX IQ Motor initialization syntax using config values
left_motor = Motor(config.LEFT_MOTOR_PORT, False)
right_motor = Motor(config.RIGHT_MOTOR_PORT, True) 

def main():
    brain.screen.print("Mode: Tank Drive")

    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Applied DEADBAND from central config
        if abs(left_speed) < config.DEADBAND: left_speed = 0
        if abs(right_speed) < config.DEADBAND: right_speed = 0

        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)

if __name__ == "__main__":
    main()
