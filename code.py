# test1.py - packet reliablity test

import time
import os


f1 = open("test1.log", "a")
f1.write("start {\n")
f1.write("}\n")
os.sync()





def main():
    try:
        # if flash is writable, send results to file then reboot
        filename = "{}__{}.txt".format(board.board_id, AsciiHex(soc.cpu.uid))
        with open(filename, "w") as fh:
            GenerateResults(fh)
        soc.reset()
    except:
        # if flash is read-only, send results to stdout
        GenerateResults(sys.stdout)

# make it so ################################################################

main()


