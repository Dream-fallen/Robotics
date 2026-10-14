from vex import *

# ---- HARDWARE SETUP ----
brain = Brain()
controller = Controller()
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 

DEADBAND = 10 # Ignore joystick movements less than 10%

def main():
    brain.screen.print("Mode: Arcade Drive")

    while True:
        forward = controller.axis3.position() 
        turn = controller.axis4.position()     
        
        # Apply deadband to prevent drifting
        if abs(forward) < DEADBAND: forward = 0
        if abs(turn) < DEADBAND: turn = 0

        # Mix channels
        left_speed = forward + turn
        right_speed = forward - turn

        # Clamp values between -100 and 100
        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)

        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)

main()
