import sys
import signal
from zenlog import log

# from radio.radio import close_current_radio
from radio.radio import gaana

gaana.meethi_mirchi()

# from radio.radio import init_ctrl_c
# import radio.trackinfo.trackinfo as tracks

# from radio.gaana.handler import ctrl_c_exit




# def signal_handler(sig, frame):
#     log.info("saving songs information before quitting")
#     # close_current_radio()
#     ctrl_c_exit.set()

#     # print all played tracks during he session
#     print(tracks.track_list)

#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)
# signal.pause()

# if __name__ == "main":
#     print("hmm")
#     gaana.meethi_mirchi()