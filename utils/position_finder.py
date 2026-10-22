from vex import *
import config

def main():
    controller = config.controller
    brain = config.brain
    # We will tune the ARM_MOTOR in this example
    motor = config.ARM_MOTOR
    
    brain.screen.clear_screen()
    brain.screen.print("POS FINDER: Use L-Stick to move")
    brain.screen.print("Check Brain for Degree value")

    while True:
        speed = controller.axisA.position()
        if abs(speed) < config.DEADBAND:
            motor.stop()
        else:
            motor.spin(FORWARD, speed, PERCENT)
        
        # Display the current position in real-time
        brain.screen.set_cursor(3, 1)
        brain.screen.print(f"Pos: {motor.position(DEGREES)} deg   ")
        
        wait(20, MSEC)

if __name__ == "__main__":
    main()
