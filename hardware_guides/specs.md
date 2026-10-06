# Flop (Hero Bot) specifications

This file documents the physical characteristics, structural constraints, and default port allocations for **Flop**, our standard Hero Bot build for the **VIQRC Level Up** game. 

---

## Physical Constraints & Sizing

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Max Starting Size** | 11” Width x 20” Length x 15” Height | `nil` |
| **Horizontal Expansion** | Max 24” total in any direction | *Caution:* Stock Flop can accidentally extend past 24” if the arm swings fully flat. |
| **Vertical Expansion** | Unlimited during the match | Flop expands vertically to reach the Level 3 scoring goal. |
| **Game Object Capacity**| Max **1 Bean Bag** at a time | The intake is strictly designed for single-possession/plowing limits. |

---

## Mechanical Build Details

### Drivetrain
* **Configuration:** 4-wheel drive powered by **2 Smart Motors**.
* **Wheel Configuration:** Standard rubber tires in the rear for traction; **Omni-Wheels** in the front to ensure a tight turning radius and smoother steering.
* **Power Delivery:** A continuous chain and sprocket system runs along the chassis side beams to tie the front and rear wheels together.
* **Gear Ratio:** `2:1` (Chain-driven setup favoring quick field traversal across the 6' x 8' arena).

### Intake Mechanism
* **Design:** Flap intake using custom tank tread rollers and flexible intake flaps wrapped around sprockets. 
* **Function:** Explicitly built to grab, flatten, and pull soft, friction-prone Level Up bean bags into a curved plastic slide.

### Flipping Arm
* **Mechanism:** Long 2-bar pivoting arm structure.
* **Gear Ratio:** High-torque gear train (Uses large compound gearing to create the immense lifting power needed to sling the intake overhead).

---

## Default Smart Port Allocation

These port assignments correspond to the standard building guide wiring. Ensure your Python or C++ configuration objects point to these specific pins.

| Smart Port | Assigned Hardware Component | API Code Handle | Notes |
| :---: | :--- | :--- | :--- |
| **Port 1** | Left Drivetrain Motor | `LeftMotor` | Inverted/reversed direction configuration. |
| **Port 6** | Right Drivetrain Motor | `RightMotor` | Standard rotation. |
| **Port [X]** | Arm Lift Motor | `ArmMotor` | Controls the high-torque lifting 2-bar gear. |
| **Port [Y]** | Intake Roller Motor | `IntakeMotor` | Controls the tank tread flap roller. |
| **Optional**| Bumper Switch Sensor | `BumperSensor` | Mounted to front bumper for field boundary detection. |
| **Optional**| AI Vision Sensor | `AIVision` | Mounted to the arm to track bean bag positions. |

---

## Known Mechanical Issues

When designing custom programs or starting your engineering notebooks, keep these limitations in mind:

1. **Center of Mass (The "Tipper"):** Because the flap intake is heavy and sits on a long arm lever, raising the arm too fast causes the robot's center of gravity to shift dangerously. The bot can easily tip over backward if driving while "flopping."
2. **Horizontal Extension Violations:** If the arm is fully lowered or fully extended backward, double-check that your bumper-to-intake length stays under the official 24-inch boundary rule.
