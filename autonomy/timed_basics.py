from vex import *

# ---- HARDWARE SETUP ----
# FIX: Removed the V5 gear settings for VEX IQ compatibility
left_motor = Motor(Ports.PORT1, False)
right_motor = Motor(Ports.PORT6, True) 

def main():
    # Drive forward for 2 seconds
    left_motor.spin(FORWARD, 50, PERCENT)
    right_motor.spin(FORWARD, 50, PERCENT)
    wait(2, SEC) # FIX: Changed SECONDS to SEC
    
    # Stop
    left_motor.stop()
    right_motor.stop()
    wait(0.5, SEC) # FIX: Changed SECONDS to SEC
    
    # Turn right for 1 second
    left_motor.spin(FORWARD, 40, PERCENT)
    right_motor.spin(REVERSE, 40, PERCENT)
    wait(1, SEC) # FIX: Changed SECONDS to SEC
    
    left_motor.stop()
    right_motor.stop()

main()
