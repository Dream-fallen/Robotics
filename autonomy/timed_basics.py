from vex import *
import config

# Aliases from config.py
# We use the DRIVETRAIN object for high-level timed movement
drivetrain = config.DRIVETRAIN
brain = config.brain

def main():
    brain.screen.clear_screen()
    brain.screen.print("Mode: Timed Open-Loop")
    wait(1, SECONDS) 

    # --- 1. Drive Forward ---
    # Set the speed for the drivetrain
    drivetrain.set_drive_velocity(50, PERCENT)
    
    # Start driving forward
    drivetrain.drive(FORWARD)
    wait(2, SECONDS) # Corrected constant from SEC to SECONDS
    
    # Stop
    drivetrain.stop()
    wait(0.5, SECONDS) 

    # --- 2. Turn Right ---
    # Set the turn speed
    drivetrain.set_turn_velocity(40, PERCENT)
    
    # Start turning right
    drivetrain.turn(RIGHT)
    wait(1, SECONDS) 
    
    # Stop
    drivetrain.stop()
    
    brain.screen.print("Timed Sequence Complete!")

if __name__ == "__main__":
    main()
