# TP5

**In the following TPs, you'll use the tools acquired during the previous classes on
 a robotic hexapod in order to create a walking gait. In this
 particular TP, you'll check the mechanical integrity of your robot,
 and you'll configure the robot in order to begin the walking gait development **

1. Set up a simple demonstration of your inverse kinematic
implementation. 30 min max. You'll use only one the leg from your hexapod. The demonstration will be a success if you manage to do the following steps :
a) go to x=170, y=-45, z=35
b) go to x=170, y=-45, z=0
c) go to x=170, y=-45, z=35
d) go to x=170, y=0, z=35
e) go to x=170, y=0, z=0
f) go to x=170, y=0, z=35
g) go to x=170, y=45, z=35
h) go to x=170, y=45, z=0
i) go to x=170, y=45, z=35 
j) start over from a)
-> The delay between each step is up to you. 1 sec is a safe first try value.

2. You'll be given an Hexapod, tighten each screw, verify the
connections. Do not underestimate Murphy.

3. Set the correct ID for each one of the 18 motors. Allowed IDs are 11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53, 61, 62, 63. The ID convention will be showed in class.

4. Go to the pypot's documentation page and read about the
'autodetect_robot' functionality and the JSON dumping system. Then
make it work for your robot

5. How would you do to make your hexapod walk? Research, discuss and
conquer the world.
