#!/usr/bin/python3

# a program that prints all numbers from 0 to 98 in decimal and in hexadecimal

for i in range(0, 99):
    print("{} = 0x{}".format(i, hex(i)[2:]))
