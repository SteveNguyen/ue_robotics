# TP4

**The aim of this TP is to solve the inverse kinematic problem on a 3
  joint leg, using simple trigonometry. Then implement the solution and test
  it on a robotic leg.**

1. Solve the inverse kinematic problem : Knowing P3(x3, y3, z3),
L1, L2 and L3, find theta1, theta2, theta3. What is the fundamental
difference between the direct and the inverse kinematic problem?

2. Adapt your solution to your robotic leg, i.e. make sure that your
solution is valid if you replace motorX.currentPosition by thetaX.

3. Implement your solution using python and pypot.

**NOTE:**
Google these if you are in need of a reminder :
- SOH CAH TOA
- Al-Kashi

Every student shall write the answers to 1. and 2. on his/her paper
version of "leg.pdf". Your work will be collected before the end of
the class (1 per student). Clean work expected. A solution will be
given.

The 3. implementation is due for the start of TP5 (1 implementation
per team). You'll then have a few minutes to prepare your setup and
demonstrate its functionality. Expected format :
A file named "inverse_kinematics.py" with a function "leg_ik(x, y, z, l1=L1, l2=L2, l3=L3, other needed parameters)" that
returns the angles [theta1,
theta2, theta3] in ° that need to be applied to the motors in order to
reach [x, y , z].
