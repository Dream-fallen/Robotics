# Code Reference Guide

This reference guide maps out the standard API designations for the **VEX IQ (2nd generation) Controller** and basic robot components. Use this file to identify how hardware variables relate to your **Python** and **C++** code structures.

---

## Controller Inputs Mapping

The VEX IQ 2nd Generation Controller features 4 Analog Joystick Axes and 10 Digital Buttons (including the L3/R3 joystick clicks).

### Joystick Axes
Each axis returns an integer value ranging from **`-100` to `+100`** (`0` when centered).

| Physical Hardware Input | Python API Property | C++ API Object |
| :--- | :--- | :--- |
| **Left Joystick (Vertical)** | `controller.axisA` | `Controller.AxisA` or `Controller.Axis3` |
| **Left Joystick (Horizontal)** | `controller.axisB` | `Controller.AxisB` or `Controller.Axis4` |
| **Right Joystick (Horizontal)** | `controller.axisC` | `Controller.AxisC` or `Controller.Axis1` |
| **Right Joystick (Vertical)** | `controller.axisD` | `Controller.AxisD` or `Controller.Axis2` |

### 🎛️ Action Buttons
Buttons return boolean values: `True` / `1` when actively pressed, and `False` / `0` when released.

| Physical Hardware Input | Python API Property | C++ API Object |
| :--- | :--- | :--- |
| **Front Left Shoulder (Top)** | `controller.buttonLUp` | `Controller.ButtonLUp` |
| **Front Left Shoulder (Bottom)** | `controller.buttonLDown` | `Controller.ButtonLDown` |
| **Front Right Shoulder (Top)** | `controller.buttonRUp` | `Controller.ButtonRUp` |
| **Front Right Shoulder (Bottom)** | `controller.buttonRDown` | `Controller.ButtonRDown` |
| **Left Button Pad (Top)** | `controller.buttonEUp` | `Controller.ButtonEUp` |
| **Left Button Pad (Bottom)** | `controller.buttonEDown` | `Controller.ButtonEDown` |
| **Right Button Pad (Top)** | `controller.buttonFUp` | `Controller.ButtonFUp` |
| **Right Button Pad (Bottom)** | `controller.buttonFDown` | `Controller.ButtonFDown` |
| **Left Joystick Press** | `controller.buttonL3` | `Controller.ButtonL3` |
| **Right Joystick Press** | `controller.buttonR3` | `Controller.ButtonR3` |

---

## Robot Parts & Smart Ports

The VEX IQ (2nd gen) Brain includes **12 Smart Ports** numbered 1 through 12. Any Smart Port can accept any VEX IQ peripheral device dynamically.

### Standard Coding Declarations

#### 1. Smart Motors
* **Python:** `motor = Motor(Ports.PORT1)`
* **C++:** `vex::motor Motor1 = vex::motor(vex::PORT1);`

#### 2. Drivetrain Configuration (2-Motor Setup)
* **Python:** 
  ```python
  left_motor = Motor(Ports.PORT1, REVERSE)
  right_motor = Motor(Ports.PORT6)
  drivetrain = Drivetrain(left_motor, right_motor, 200, 320) # wheel_travel, track_width
  ```
* **C++:**
  ```cpp
  vex::motor LeftMotor = vex::motor(vex::PORT1, true);
  vex::motor RightMotor = vex::motor(vex::PORT6, false);
  vex::drivetrain Drivetrain1 = vex::drivetrain(LeftMotor, RightMotor);
  ```

#### 3. Optical Sensor
* **Python:** `optical = Optical(Ports.PORT3)`
* **C++:** `vex::optical Optical3 = vex::optical(vex::PORT3);`

#### 4. Distance Sensor
* **Python:** `distance = Distance(Ports.PORT4)`
* **C++:** `vex::distance Distance4 = vex::distance(vex::PORT4);`

#### 5. Bumper Switch
* **Python:** `bumper = Bumper(Ports.PORT5)`
* **C++:** `vex::bumper Bumper5 = vex::bumper(vex::PORT5);`

---

## Quick Code Implementation Snippet

### Reading Controller Input (Polling Loop)

#### Python
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

#### C++
```cpp
int main() {
    while(true) {
        // Read Analog Stick for driving
        int forwardSpeed = Controller.AxisA.position();
        
        // Check if a shoulder button is pressed to activate an attachment
        if (Controller.ButtonLUp.pressing()) {
            ArmMotor.spin(vex::forward);
        } else {
            ArmMotor.stop();
        }
        
        vex::wait(20, vex::msec); // Prevents CPU hogging
    }
}
```
