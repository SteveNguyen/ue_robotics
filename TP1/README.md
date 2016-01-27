# TP1

**The aim of this TP is to solve the direct kinematic problem on a 3
  joint leg, using simple trigonometry. Then implement the solution. 
The implementation will be tested on a robotic leg later on.

1. Solve the direct kinematic problem : Knowing theta1, theta2, theta3,
L1, L2 and L3, find P1(x1, y1, z1), P2(x2, y2, z2) and P3(x3, y3, z3).

2. Adapt your solution to your robotic leg, i.e. make sure that your
solution is valid if you replace thetaX by
motorX.currentPosition. What is the (x=0, y=0, z=0) point of the real leg?

3. Find L1, L2, L3 and any other needed measure. Use the information provided by the "origin.pdf" document.

4. Implement your solution using python.

**NOTES:**
The answers to 1. 2. and 3. shall be written on a paper
version of "leg.pdf". Your work will be collected before the end of
the class (1 per student). Clean work expected. A solution will be
given afterwards.

The 4. implementation is due for the start of TP4 (1 implementation
per team). You'll then have a few minutes to prepare your setup and
demonstrate its functionality. Expected format :
A file named "direct_kinematics.py" with a function "leg_dk(theta1,
theta2, theta3, l1=L1, l2=L2, l3=L3, other needed parameters)" that
returns the position [x, y, z] of the end of the leg.

l1 = 51
l2 = 63.7
l3 = 93
alpha = 20.69
beta = 5.06


As a quick verification here are the solutions for some values of Theta1, Theta2, Theta3 (in mm with an accepted error of +/- 1mm):

0°,0°,0°:  [118.79, 0.0, -115.14]

90°,0°,0°:  [0.0, 118.79, -115.14]

180°, -30.501°, -67.819°:  [-64.14, 0.0, -67.79]

0°, -30.645°, 38.501°:  [203.23, 0.0, -14.30]
