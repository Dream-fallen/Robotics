from vex import *

# ---- BRAIN & INTERNAL SENSORS ----
brain = Brain()
INERTIAL = Inertial()  # Built-in sensor, no port required!

# ---- MOTORS ----
LEFT_MOTOR = Motor(Ports.PORT1, False)
RIGHT_MOTOR = Motor(Ports.PORT6, True)
ARM_MOTOR = Motor(Ports.PORT2, False)
CLAW_MOTOR = Motor(Ports.PORT3, True)

# ---- SENSORS ----
DISTANCE = Distance(Ports.PORT11)
OPTICAL = Optical(Ports.PORT12)

# ---- CONSTANTS ----
WHEEL_CIRCUMFERENCE = 7.874 # 200mm wheels
DEADBAND = 10
