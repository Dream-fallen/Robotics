from vex import *
import config

# ---- PRESETS ----
ARM_POSITIONS = {
    "IDLE": 0,
    "PICKUP": 450,
    "SCORE": 900
}

CLAW_POSITIONS = {
    "OPEN": 0,
    "CLOSED": 120
}

# ---- HELPER FUNCTIONS ----
def move_arm(position_name, speed=50):
    if position_name in ARM_POSITIONS:
        target = ARM_POSITIONS[position_name]
        config.ARM_MOTOR.set_velocity(speed, PERCENT)
        config.ARM_MOTOR.spin_to_position(target, DEGREES)

def move_claw(position_name, speed=50):
    if position_name in CLAW_POSITIONS:
        target = CLAW_POSITIONS[position_name]
        config.CLAW_MOTOR.set_velocity(speed, PERCENT)
        config.CLAW_MOTOR.spin_to_position(target, DEGREES)

def handle_driver_control():
    # 0 = Arcade, 1 = Tank
    drive_mode = 0 
    controller = config.controller
    brain = config.brain
    
    brain.screen.clear_screen()
    brain.screen.print("Mode: Arcade (Press L3 to Toggle)")

    while True:
        # 1. MODE TOGGLE (L3 Joystick Press)
        if controller.buttonL3.pressing():
            drive_mode = 1 if drive_mode == 0 else 0
            # Update Brain Screen
            brain.screen.clear_screen()
            mode_text = "Mode: Tank" if drive_mode == 1 else "Mode: Arcade"
            brain.screen.print(mode_text)
            wait(300, MSEC) # Debounce to prevent rapid flickering

        # 2. DRIVE LOGIC
        if drive_mode == 0: # Arcade (L-Stick only)
            forward = controller.axisA.position()
            turn = controller.axisB.position()
            
            if abs(forward) < config.DEADBAND: forward = 0
            if abs(turn) < config.DEADBAND: turn = 0
            
            l_speed = max(-100, min(100, forward + turn))
            r_speed = max(-100, min(100, forward - turn))
            
        else: # Tank (Both sticks Vertical)
            l_speed = controller.axisA.position()
            r_speed = controller.axisD.position()
            
            if abs(l_speed) < config.DEADBAND: l_speed = 0
            if abs(r_speed) < config.DEADBAND: r_speed = 0

        # Apply movement to motors
        config.LEFT_MOTOR.spin(FORWARD, l_speed, PERCENT)
        config.RIGHT_MOTOR.spin(FORWARD, r_speed, PERCENT)

        # 3. ARM & CLAW LOGIC (Presest Triggers)
        # Arm: L-Shoulder Buttons
        if controller.buttonLUp.pressing():
            move_arm("SCORE")
        elif controller.buttonLDown.pressing():
            move_arm("PICKUP")

        # Claw: R-Shoulder Buttons
        if controller.buttonRUp.pressing():
            move_claw("OPEN")
        elif controller.buttonRDown.pressing():
            move_claw("CLOSED")
            
        wait(20, MSEC)

if __name__ == "__main__":
    handle_driver_control()
