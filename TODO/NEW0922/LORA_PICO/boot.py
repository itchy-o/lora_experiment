# boot.py

import storage
import usb_hid
import usb_midi

# writable for CPy
#storage.remount("/", readonly=False)

usb_hid.disable()
usb_midi.disable()

#eof
