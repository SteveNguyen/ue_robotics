import itertools
import time
import numpy
import pypot.dynamixel


if __name__ == '__main__':

    # we first open the Dynamixel serial port
    with pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000) as dxl_io:

        # we can scan the motors
        found_ids = dxl_io.scan()  # this may take several seconds
        print 'Detected:', found_ids

        # we power on the motors
        dxl_io.enable_torque(found_ids)

        # we get the current positions
        print 'Current pos:', dxl_io.get_present_position(found_ids)

        # we create a python dictionnary: {id0 : position0, id1 : position1...}
        pos = dict(zip(found_ids, itertools.repeat(0)))
        print 'Cmd:', pos

        # we send these new positions
        dxl_io.set_goal_position(pos)
        time.sleep(1)  # we wait for 1s

        # we get the current positions
        print 'New pos:', dxl_io.get_present_position(found_ids)

        # we power off the motors
        dxl_io.disable_torque(found_ids)
        time.sleep(1)  # we wait for 1s
