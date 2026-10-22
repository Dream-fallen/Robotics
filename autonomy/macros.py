from vex import *
import config
import auto_pro as ap # Import your Pro Auto functions

def pick_up_object():
    """Macro: Drives forward slightly, lowers arm, closes claw, lifts arm"""
    ap.drive_straight(5, 30) # Approach
    ap.move_arm("PICKUP")
    ap.move_claw("CLOSED")
    wait(500, MSEC)
    ap.move_arm("SCORE")

def score_at_goal():
    """Macro: Drives to goal, opens claw, returns to idle"""
    ap.drive_straight(15, 40)
    ap.move_claw("OPEN")
    wait(500, MSEC)
    ap.move_arm("IDLE")
    ap.move_claw("CLOSED") # Reset claw

def main():
    # Now your main autonomous script is incredibly simple:
    pick_up_object()
    ap.turn_to_angle(90)
    score_at_goal()
