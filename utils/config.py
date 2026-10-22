from vex import *

# ==============================================================================
# PORT MAPPING
# Change these values if you move a cable to a different port on the brain
# ==============================================================================
PORT_LEFT_DRIVE  = Ports.PORT1
PORT_RIGHT_DRIVE = Ports.PORT6
PORT_ARM         = Ports.PORT2
PORT_CLAW        = Ports.PORT3
PORT_DISTANCE    = Ports.PORT11
PORT_OPTICAL     = Ports.PORT12
PORT_BUMPER      = Ports.PORT5  # Added as a placeholder for common builds

# ==============================================================================
# HARDWARE INITIALIZATION
# ==============================================================================

# Brain & Internal Sensors
brain = Brain()
INERTIAL = Inertial() 

# Motors
# (Using the port variables defined above)
LEFT_MOTOR  = Motor(PORT_LEFT_DRIVE, FORWARD)
RIGHT_MOTOR = Motor(PORT_RIGHT_DRIVE, REVERSE)
ARM_MOTOR   = Motor(PORT_ARM, FORWARD)
CLAW_MOTOR  = Motor(PORT_CLAW, REVERSE)

# Sensors
DISTANCE = Distance(PORT_DISTANCE)
OPTICAL  = Optical(PORT_OPTICAL)
BUMPER   = Bumper(PORT_BUMPER)

# Controller
controller = Controller()

# Drivetrain
# Parameters: (left_motor, right_motor, wheel_travel, track_width)
# wheel_travel: 200mm (Standard VEX IQ wheel)
# track_width: Distance between left and right wheels (approx 170mm, adjust as needed)
DRIVETRAIN = Drivetrain(LEFT_MOTOR, RIGHT_MOTOR, 200, 170)

# ==============================================================================
# CONSTANTS
# ==============================================================================
WHEEL_CIRCUMFERENCE = 7.874 # 200mm wheels in inches (approx)
DEADBAND = 10               # Minimum joystick value to trigger movement
