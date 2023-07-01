# test1.py - packet reliablity test

print("0 is this visible?")

import time
import os
import adafruit_rfm9x

#import rfm9x_header
#import rfm9x_node1
#import rfm9x_node1_ack
#import rfm9x_node1_bonnet
#import rfm9x_node2
#import rfm9x_node2_ack
#import rfm9x_rpi_interrupt
#import rfm9x_rpi_simpletest
#import rfm9x_simpletest
#import rfm9x_transmit

def main():
    print("1 is this visible?")
    f1 = open("test1.log", "a")
    f1.write("start {\n")
    f1.write("}\n")
    os.sync()
    print("the end")

main()
