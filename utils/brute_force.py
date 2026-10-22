from vex import *
import config

def main():
    controller = config.controller
    
    while True:
        # Motor Tests
        config.LEFT_MOTOR.spin(FORWARD, 50 if controller.buttonLUp.pressing() else 0, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, 50 if controller.buttonLDown.pressing() else 0, PERCENT)
        config.ARM_MOTOR.spin(FORWARD, 50 if controller.buttonRUp.pressing() else 0, PERCENT)
        config.CLAW_MOTOR.spin(FORWARD, 50 if controller.buttonRDown.pressing() else 0, PERCENT)
        
        # Sensor Tests (Print to Brain)
        if controller.buttonL3.pressing():
            config.brain.screen.clear_screen()
            config.brain.screen.print(f"Dist: {config.DISTANCE.distance(MM)}mm")
            config.brain.screen.print(f"Color: {config.OPTICAL.color()}")
            
        wait(20, MSEC)

if __name__ == "__main__":
    main()
