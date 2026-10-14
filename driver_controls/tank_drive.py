from vex import *

# ---- HARDWARE SETUP ----
brain = Brain()
controller = Controller()
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True) 

DEADBAND = 10

def main():
    brain.screen.print("Mode: Tank Drive")

    while True:
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        if abs(left_speed) < DEADBAND: left_speed = 0
        if abs(right_speed) < DEADBAND: right_speed = 0

        left_motor.spin(FORWARD, left_speed, PERCENT)
        right_motor.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)

main()
