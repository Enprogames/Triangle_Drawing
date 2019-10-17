import math

def trig(side_a, side_b, side_c, angle_a, angle_b, angle_c=90):

    if side_a >= 1:
        if side_b >= 1: # side a and b exist
            side_c = (side_a ** 2 + side_b ** 2) ** 0.5
            angle_a = math.degrees(math.atan(side_a/side_b))
            angle_b = math.degrees(math.atan(side_b/side_a))
        elif side_c >= 1: # side a and c exist
            side_b = (side_c ** 2 - side_a ** 2)  ** 0.5
            angle_a = math.degrees(math.asin(side_a/side_c))
            angle_b = math.degrees(math.acos(side_a/side_c))
        elif angle_b >= 1: # side a and angle b exist
            side_b = side_a / math.tan(angle_b)
            side_c = side_a / math.sin(angle_b)
            angle_a = math.degrees(math.atan(side_a/side_b))
        elif angle_a >= 1: # side a and angle c exist
            side_b = side_a / math.tan(angle_a)
            side_c = side_a / math.sin(angle_a)
            angle_b = math.degrees(math.atan(side_b/side_a))
    elif side_b >= 1:
        if side_c >= 0:
            side_a = ((side_c**2) - (side_b**2))**0.5
            angle_a = math.degrees(math.acos(side_b/side_c))
            angle_b = math.degrees(math.asin(side_b/side_c))
        elif side_a >= 0:
            side_c = ((side_a**2)+(side_b**2))**0.5
            angle_a = math.degrees(math.atan(side_a/side_b))
            angle_b = math.degrees(math.atan(side_b/side_a))
        elif angle_b >= 1:
            print()
        elif angle_a >= 1:
            print()

    elif side_c >= 1:
        print()
    else:
        side_a = 3
        side_b = 4
        side_c = 5
        angle_b = math.degrees(math.atan(side_b/side_a))
        angle_a = math.degrees(math.atan(side_a/side_b))

    return [side_a, side_b, side_c, angle_a, angle_b]