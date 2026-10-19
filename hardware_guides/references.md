# Code Reference Guide (Python)

This reference guide maps out the standard API designations for the **VEX IQ (2nd generation) Controller** and basic robot components. Use this file to identify how hardware variables relate to your **Python** code structures.

---

## Controller Inputs Mapping

The VEX IQ 2nd Generation Controller features 4 Analog Joystick Axes and 10 Digital Buttons (including the L3/R3 joystick clicks).

### Joystick Axes
Each axis returns an integer value ranging from **`-100` to `+100`** (`0` when centered).

| Physical Hardware Input | Python API Property |
| :--- | :--- |
| **Left Joystick (Vertical)** | `controller.axisA` |
| **Left Joystick (Horizontal)** | `controller.axisB` |
| **Right Joystick (Horizontal)** | `controller.axisC` |
| **Right Joystick (Vertical)** | `controller.axisD` |

### 🎛️ Action Buttons
Buttons return boolean values: `True` when actively pressed, and `False` when released.

| Physical Hardware Input | Python API Property |
| :--- | :--- |
| **Front Left Shoulder (Top)** | `controller.buttonLUp` |
| **Front Left Shoulder (Bottom)** | `controller.buttonLDown` |
| **Front Right Shoulder (Top)** | `controller.buttonRUp` |
| **Front Right Shoulder (Bottom)** | `controller.buttonRDown` |
| **Left Button Pad (Top)** | `controller.buttonEUp` |
| **Left Button Pad (Bottom)** | `controller.buttonEDown` |
| **Right Button Pad (Top)** | `controller.buttonFUp` |
| **Right Button Pad (Bottom)** | `controller.buttonFDown` |
| **Left Joystick Press** | `controller.buttonL3` |
| **Right Joystick Press** | `controller.buttonR3` |

---

## Robot Parts & Smart Ports

The VEX IQ (2nd gen) Brain includes **12 Smart Ports** numbered 1 through 12. Any Smart Port can accept any VEX IQ peripheral device dynamically.

### Standard Coding Declarations

#### 1. Smart Motors
* `motor = Motor(Ports.PORT1)`

#### 2. Drivetrain Configuration (2-Motor Setup)
```python
left_motor = Motor(Ports.PORT1, REVERSE)
right_motor = Motor(Ports.PORT6)
drivetrain = Drivetrain(left_motor, right_motor, 200, 320) # wheel_travel, track_width
```

#### 3. Optical Sensor
* `optical = Optical(Ports.PORT3)`

#### 4. Distance Sensor
* `distance = Distance(Ports.PORT4)`

#### 5. Bumper Switch
* `bumper = Bumper(Ports.PORT5)`

---

## Quick Code Implementation Snippet

### Reading Controller Input (Polling Loop)

```python
while True:
    # Read Analog Stick for driving
    forward_speed = controller.axisA.position()
    
    # Check if a shoulder button is pressed to activate an attachment
    if controller.buttonLUp.pressing():
        arm_motor.spin(FORWARD)
    else:
        arm_motor.stop()
        
    wait(20, msec) # Prevents CPU hogging
```
