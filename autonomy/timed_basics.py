from vex import *

# ---- HARDWARE SETUP ----
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 

def main():
    # Drive forward for 2 seconds
    left_motor.spin(FORWARD, 50, PERCENT)
    right_motor.spin(FORWARD, 50, PERCENT)
    wait(2, SECONDS)
    
    # Stop
    left_motor.stop()
    right_motor.stop()
    wait(0.5, SECONDS)
    
    # Turn right for 1 second
    left_motor.spin(FORWARD, 40, PERCENT)
    right_motor.spin(REVERSE, 40, PERCENT)
    wait(1, SECONDS)
    
    left_motor.stop()
    right_motor.stop()

main()
