# TP3

**The aim of this TP is to solve the direct kinematic problem on a 3
  joint leg, using simple trigonometry. Then implement the solution and test
  it on a robotic leg.**

1. Solve the direct kinematic problem : Knowing theta1, theta2, theta3,
L1, L2 and L3, find P1(x1, y1, z1), P2(x2, y2, z2) and P3(x3, y3, z3).

2. Adapt your solution to your robotic leg, i.e. make sure that your
solution is valid if you replace thetaX by
motorX.currentPosition. What is the (0, 0) point of the leg?

3. Find L1, L2, L3 and any other needed measure. Ideally, find the piece's actual dimensions instead of just
measuring them.

4. Implement your solution using python and pypot.

**NOTE:**
The answers to 1. 2. and 3. shall be written a paper
version of "leg.pdf". Your work will be collected before the end of
the class (1 per student). Clean work expected. A solution will be
given.

The 4. implementation is due for the start of TP4 (1 implementation
per team). You'll then have a few minutes to prepare your setup and
demonstrate its functionality. Expected format :
A file named "direct_kinematics.py" with a function "leg_dk(theta1,
theta2, theta3, l1=L1, l2=L2, l3=L3, other needed parameters)" that
returns the position [x, y, z] of the end of the leg.
