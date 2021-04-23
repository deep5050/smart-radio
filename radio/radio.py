# import radio.gaana.handler as gaana_handler
from zenlog import log
from threading import Event

import radio.gaana.handler as gaana_handler
from radio.gaana.handler import pehla_nasha_handler as gaana_pehla_nasha
from radio.gaana.handler import meethi_mirchi_handler as gaana_meethi_mirchi


current_radio = None
# global ctrl_c_exit

# def init_ctrl_c():
#     global ctrl_c_exit
#     ctrl_c_exit = Event()

def close_current_radio():
    # closes any opened radio
    global current_radio
    if current_radio != None:
        current_radio.close()
        log.info("Successfully closed the radio")
    else:
        log.warn("No radio is playing")


# gaana.com radio handler
class Gaana:
    def __init__(self):
        self.current_channel = None
        print("creating")

    def pehla_nasha(self):
        log.debug("called pehlanasha")
        global current_radio
        self.current_channel = "pehla_nasha"
        current_radio = gaana_handler
        gaana_pehla_nasha()

    def meethi_mirchi(self):
        log.debug("called meethi mirchi")
        global current_radio
        self.current_channel = "meethi_mirchi"
        current_radio = gaana_handler
        gaana_meethi_mirchi()


gaana = Gaana()