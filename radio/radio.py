# import radio.gaana.handler as gaana_handler
from threading import Event
from zenlog import log

import radio.gaana.handler as gaana_handler
from radio.gaana.handler import pehla_nasha_handler as gaana_pehla_nasha
from radio.gaana.handler import meethi_mirchi_handler as gaana_meethi_mirchi
from radio.gaana.handler import english_love_handler as gaana_english_love
from radio.gaana.handler import ranbindra_sangeet_handler as gaana_rabindra_sangeet
from radio.gaana.handler import toota_dil_handler as gaana_toota_dil
from radio.gaana.handler import filmy_mirchi_handler as gaana_filmy_mirchi
from radio.gaana.handler import international_hits_handler as gaana_international_hits
from radio.gaana.handler import english_retro_hits_handler as gaana_english_retro_hits
from radio.gaana.handler import mirchi_90s_handler as gaana_mirchi_90s


current_radio = None


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

    def pehla_nasha(self, visible):
        log.debug("Called pehlanasha")
        global current_radio
        self.current_channel = "pehla_nasha"
        current_radio = gaana_handler
        gaana_pehla_nasha(visible)

    def meethi_mirchi(self, visible):
        log.debug("Called meethi mirchi")
        global current_radio
        self.current_channel = "meethi_mirchi"
        current_radio = gaana_handler
        gaana_meethi_mirchi(visible)

    def english_love(self, visible):
        log.debug("Called english love")
        global current_radio
        self.current_channel = "english_love"
        current_radio = gaana_handler
        gaana_english_love(visible)

    def rabindra_sangeet(self, visible):
        log.debug("Called rabindra sangeet")
        global current_radio
        self.current_channel = "rabindra_sangeet"
        current_radio = gaana_handler
        gaana_rabindra_sangeet(visible)

    def toota_dil(self, visible):
        log.debug("Called toota dil")
        global current_radio
        self.current_channel = "toota_dil"
        current_radio = gaana_handler
        gaana_toota_dil(visible)

    def filmy_mirchi(self, visible):
        log.debug("Called filmy mirchi")
        global current_radio
        self.current_channel = "filmy mirchi"
        current_radio = gaana_handler
        filmy_mirchi_handler(visible)

    def international_hits(self, visible):
        log.debug("Called international hits")
        global current_radio
        self.current_channel = "international hits"
        current_radio = gaana_handler
        gaana_international_hits(visible)

    def english_retro_hits(self, visible):
        log.debug("Called english retro hits")
        global current_radio
        self.current_channel = "english retro hits"
        current_radio = gaana_handler
        gaana_english_retro_hits(visible)

    def mirchi_90s(self, visible):
        log.debug("Called mirchi 90s")
        global current_radio
        self.current_channel = "mirchi_90s"
        current_radio = gaana_handler
        gaana_mirchi_90s(visible)


gaana = Gaana()