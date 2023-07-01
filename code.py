# test1.py - packet reliablity test

import time
import os
import adafruit_rfm9x

print("is this visible?")



f1 = open("test1.log", "a")
f1.write("start {\n")
f1.write("}\n")
os.sync()

print("the end")




# main()


