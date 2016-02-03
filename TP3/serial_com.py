#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial


def open_serial(port, baud):
    ser = serial.Serial(port=port, baudrate=baud)
    if ser.isOpen():
        return ser
    else:
        print 'SERIAL ERROR'


def close(ser):
    ser.close()


def write_data(ser, data):
    ser.write(data)


def read_data(ser, size=1):
    return ser.read(size)


def to_hex(val):
    return chr(val)


def decode_data(data):
    res = ''
    for d in data:
        res += hex(ord(d)) + ' '

    return res

if __name__ == '__main__':

    # we open the port
    serial_port = open_serial('/dev/ttyUSB0', 1000000, timeout=0.1)

    # we create the packet for a LED ON command
    # two start bytes
    data_start = to_hex(0xff)

    # id of the motor (here 1), you need to change
    data_id = to_hex(0x01)

    # lenght of the packet
    data_lenght = to_hex(0x04)

    # instruction write= 0x03
    data_instruction = to_hex(0x03)

    # instruction parameters
    data_param1 = to_hex(0x19)  # LED address=0x19
    data_param2 = to_hex(0x01)  # write 0x01

    # checksum (read the doc)
    data_checksum = to_hex(0xdd)

    # we concatenate everything
    data = data_start + data_start + data_id + data_lenght + \
        data_instruction + data_param1 + data_param2 + data_checksum

    print decode_data(data)
    write_data(serial_port, data)

    # read the status packet (size 6)
    d = read_data(serial_port, 6)
    print decode_data(d)
