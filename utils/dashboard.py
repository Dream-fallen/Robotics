from vex import *
import config

def main():
    brain = config.brain
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        
        # Display all vital signs
        brain.screen.print(f"Heading: {config.INERTIAL.heading()} deg")
        brain.screen.set_cursor(2, 1)
        brain.screen.print(f"Dist: {config.DISTANCE.distance(MM)} mm")
        brain.screen.set_cursor(3, 1)
        brain.screen.print(f"Color: {config.OPTICAL.color()}")
        brain.screen.set_cursor(4, 1)
        brain.screen.print(f"Bumper: {config.BUMPER.pressing()}")
        brain.screen.set_cursor(5, 1)
        brain.screen.print(f"L-Pos: {config.LEFT_MOTOR.position(DEGREES)}")
        
        wait(100, MSEC) # Refresh rate

if __name__ == "__main__":
    main()
