# test1.py - packet reliablity test

import time
import os

    out.write("help('modules') {\n")
    help('modules')
    out.write("# TODO how to redirect help('modules') to output filehandle?\n")
    out.write("}\n")



def main():
    try:
        # if flash is writable, send results to file then reboot
        filename = "{}__{}.txt".format(board.board_id, AsciiHex(soc.cpu.uid))
        with open(filename, "w") as fh:
            GenerateResults(fh)
        os.sync()
        soc.reset()
    except:
        # if flash is read-only, send results to stdout
        GenerateResults(sys.stdout)

# make it so ################################################################

main()


