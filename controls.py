# Functions for controlling the claws
# By default, all claws are gripped
# p denotes prime (counter-clockwise)
# 2 means turn twice (180 degrees)

# Turn front side CW
def turnF:
    # Turn front claw 90 degrees CW
    # Ungrip claw
    # Turn front claw 90 degrees CCW
    # Grip claw

# Turn front side CCW
def turnFp:
    # Turn front claw 90 degrees CCW
    # Ungrip claw
    # Turn front clas 90 degrees CW
    # Grip claw

# Turn front side twice
def turnF2:
    # Turn front claw 180 degrees
    # Ungrip claw
    # Turn front claw 180 degrees
    # Grip claw

# Turn right side CW
def turnR:
    # Turn right claw 90 degrees CW
    # Ungrip claw
    # Turn right claw 90 degrees CCW
    # Grip claw

# Turn right side CCW
def turnRp:
    # Turn right claw 90 degrees CCW
    # Ungrip claw
    # Turn right claw 90 degrees CW
    # Grip claw

# Turn right side twice
def turnR2:
    # Turn right claw 180
    # Ungrip claw
    # Turn right claw 180
    # Grip claw

# Turn left side CW
def turnL:
    # Turn left claw 90 degrees CW
    # Ungrip claw
    # Turn left claw 90 degrees CCW
    # Grip claw

# Turn left side CCW
def turnLp:
    # Turn left claw 90 degrees CCW
    # Ungrip claw
    # Turn left claw 90 degrees CW
    # Grip claw

# Turn left side twice
def turnL2:
    # Turn left claw 180
    # Ungrip claw
    # Turn left claw 180
    # Grip claw

# Turn up side CW
def turnU:
    # Ungrip front claw
    # Ungrip back claw
    # Ungrip left claw
    # Turn right claw 90 degrees CCW (up side is now on front)

    # Grip left claw
    # Ungrip right claw
    # Turn right claw 90 degrees CW

    # Grip front claw
    # Turn front claw 90 degrees CW
    # Ungrip front claw
    # Turn front claw 90 degrees CCW

    # Turn left claw 90 degrees CCW (up side is now back to up)
    # Grip right claw
    # Ungrip left claw
    # Turn left claw 90 degrees CW
    # Grip left claw

    # Grip front claw
    # Grip back claw

# Turn up side CCW
def turnUp:
    # Ungrip front claw
    # Ungrip back claw
    # Ungrip left claw
    # Turn right claw 90 degrees CCW (up side is now on front)

    # Grip left claw
    # Ungrip right claw
    # Turn right claw 90 degrees CW

    # Grip front claw
    # Turn front claw 90 degrees CCW
    # Ungrip front claw
    # Turn front claw 90 degrees CW

    # Turn left claw 90 degrees CCW (up side is now back to up)
    # Grip right claw
    # Ungrip left claw
    # Turn left claw 90 degrees CW
    # Grip left claw

    # Grip front claw
    # Grip back claw

# Turn up side twice
def turnU2:
    # Ungrip front claw
    # Ungrip back claw
    # Ungrip left claw
    # Turn right claw 90 degrees CCW (up side is now on front)

    # Grip left claw
    # Ungrip right claw
    # Turn right claw 90 degrees CW

    # Grip front claw
    # Turn front claw 180 degrees
    # Ungrip front claw
    # Turn front claw 180 degrees

    # Turn left claw 90 degrees CCW (up side is now back to up)
    # Grip right claw
    # Ungrip left claw
    # Turn left claw 90 degrees CW
    # Grip left claw

    # Grip front claw
    # Grip back claw

# Turn down side CW
def turnD:

# Turn down side CCW
def turnDp:

# Turn down side twice
def turnD2:


# Turn back side CW
def turnB:
    # Turn up back 90 degrees CW
    # Ungrip claw
    # Turn up back 90 degrees CCW
    # Grip claw

# Turn back side CCW
def turnBp:
    # Turn back claw 90 degrees CCW
    # Ungrip claw
    # Turn back claw 90 degrees CW
    # Grip claw

# Turn back side twice
def turnB2:
