import math

constL1 = 51
constL2 = 63.7
constL3 = 93
# Angle to match the theory with reality for theta 2 (measures of the triangle are 22.5, 60.7, 63.7). => Angle =  -20.69
theta2Correction = -20.69
# Same goes for theta 3 : +90 - 20.69 - a. Where a = asin(8.2/93) = 5.06
theta3Correction = 90 + theta2Correction - 5.06

# Given the sizes (a, b, c) of the 3 sides of a triangle, returns the angle between a and b using the alKashi theorem.
def alKashi(a, b, c):
    value = ((a*a)+(b*b)-(c*c))/(2*a*b)
    #Note : to get the other altenative, simply change the sign of the return :
    return -math.acos(value)


# Computes the direct kinematics of a leg in the leg's frame
# Given the angles (theta1, theta2, theta3) of a limb with 3 rotational axes separated by the distances (l1, l2, l3),
# returns the destination point (x, y, z)
def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2,l3=constL3) :
    theta1 = theta1 * math.pi / 180.0
    theta2 = (theta2 - theta2Correction) * math.pi / 180.0
    theta3 = -(theta3 - theta3Correction) * math.pi / 180.0

    planContribution = l1 + l2*math.cos(theta2) + l3*math.cos(theta2 + theta3)

    x = math.cos(theta1) * planContribution
    y = math.sin(theta1) * planContribution
    z = -(l2 * math.sin(theta2) + l3 * math.sin(theta2 + theta3))

    return [x, y, z]

# Computes the inverse kinematics of a leg in the leg's frame
# Given the destination point (x, y, z) of a limb with 3 rotational axes separated by the distances (l1, l2, l3),
# returns the angles to apply to the 3 axes
def computeIK(x, y, z, l1=constL1, l2=constL2,l3=constL3) :
    # theta1 is simply the angle of the leg in the X/Y plane. We have the first angle we wanted.
    theta1 = math.atan2(y, x)

    # Distance between the second motor and the projection of the end of the leg on the X/Y plane
    xp = math.sqrt(x*x+y*y)-l1
    if (xp < 0) :
        print("Destination point too close")
        xp = 0

    # Distance between the second motor arm and the end of the leg
    d = math.sqrt(math.pow(xp,2) + math.pow(z,2))
    if (d > l2+l3):
        print("Destination point too far away")
        d = l2+l3

    # Knowing l2, l3 and d, theta1 and theta2 can be computed using the Al Kashi law
    theta2 = alKashi(l2, d, l3) - math.atan2(z, xp)
    theta3 = math.pi - alKashi(l2, l3, d)

    return [modulo180(math.degrees(theta1)), modulo180(math.degrees(theta2) + theta2Correction), modulo180(math.degrees(theta3) + theta3Correction)]

#Takes an angle that's between 0 and 360 and returns an angle that is between -180 and 180
def modulo180(angle) :
    if (-180 < angle < 180) :
        return angle

    angle  = angle % 360
    if (angle > 180) :
        return -360 + angle

    return angle
