from threading import Event
from zenlog import log
import signal
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys


track_list = []

browser = None


def open_browser(visible):
    global browser
    _options = Options()

    if not visible:
        _options.add_argument("--headless")
        log.debug("Browser started in headless mode")
        _options.add_argument("window-size=1024x768")
        log.debug("Browser window size: 1024x768")

    browser = Chrome(options=_options)

    # if not visible:
    #     browser.maximize_window()
    #     log.debug("Browser window maximized")


global ctrl_c_exit
ctrl_c_exit = Event()


def close_browser():
    global browser
    browser.quit()
    log.debug("Browser closed")


def signal_handler(sig, frame):
    log.info("\nSaving songs information before quitting")
    with open("tracks.txt", "w") as f:
        for index in range(0, len(track_list)):
            f.write("{}\n".format(str(track_list[index])))
        f.close()

    close_browser()
    ctrl_c_exit.set()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
# signal.pause()


def generic_handler(URL, station, default_title, visible=False):
    open_browser(visible)
    global browser
    global track
    global track_list

    try:
        browser.get(URL)
    except Exception as e:
        log.critical(e)
        browser.quit()
        sys.exit(0)

    _title = None
    _artists_or_album = None

    try:
        # get the big play button and click
        big_play_button = browser.find_element_by_xpath("//a[@id='p-list-play_all']")
        big_play_button.click()
        log.info("Playing now")

        # sleeping for 5 senconds just to load everything properly (specially the track info),
        # depends on the network speed and broswer
        
        sleep(5)

        last_track_title = ""

        while True:
            _title = browser.find_element_by_xpath("//h3[@id='stitle']").text
            _artists_or_album = browser.find_element_by_xpath("//p[@id='atitle']").text

            if _title == default_title:
                # log.debug("Skipping default title")
                # skip station default audio ? IDN what is it called LOL :)
                sleep(30)
                continue

            if _title != last_track_title:
                log.info(
                    "Song => title: {}, artist(s)/album: {}".format(
                        _title, _artists_or_album
                    )
                )

                track_list.append(
                    {"title": _title, "artists_or_album": _artists_or_album}
                )

            last_track_title = _title

            # checking for new track after every 30 seconds
            # checking frequently because 
            # TODO: other approach to see the chenges in track

            # ctrl_c_exit.wait(30)
            sleep(30)
        # at this point we should close the browser
        # close_browser()

    except Exception as e:
        log.critical(str(e))
        close_browser()
        sys.exit(0)


def pehla_nasha_handler(visible):
    log.info("Starting radio: Mirchi pehla nasha")
    log.warn("Can not fecth song information from this station")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-pehlanasha",
        "pehla_nasha",
        "Mirchi Play Started...",
        visible,
    )


def meethi_mirchi_handler(visible):
    log.info("Starting radio: Meethi mirchi")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-meethi-mirchi",
        "meethi_mirchi",
        "Mirchi Play Started...",
        visible,
    )


def english_love_handler(visible):
    log.info("Starting radio: Mirchi english love")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-english-love",
        "english_love",
        "Mirchi Play Started...",
        visible,
    )


def ranbindra_sangeet_handler(visible):
    log.info("Starting radio: Mirchi ranbindra sangeet")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-rabindra-sangeet",
        "rabindra_sangeet",
        "Mirchi Play Started...",
        visible,
    )


def toota_dil_handler(visible):
    log.info("Starting radio: Mirchi toota dil")
    generic_handler(
        "https://gaana.com/radio/mirchi-toota-dil",
        "toota_dil",
        "Mirchi Play Started...",
        visible,
    )


def filmy_mirchi_handler(visible):
    log.info("Starting radio: Filmy mirchi")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-filmy-mirchi",
        "filmy_mirchi",
        "Mirchi Play Started...",
        visible,
    )


def international_hits_handler(visible):
    log.info("Starting radio: Mirchi nternational hits")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-international-hits",
        "international_hits",
        "Mirchi Play Started...",
        visible,
    )


def english_retro_hits_handler(visible):
    log.info("Starting radio: Mirchi english retro hits")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-english-retro",
        "english_retro",
        "Mirchi Play Started...",
        visible,
    )


def mirchi_90s_handler(visible):
    log.info("Starting radio: Mirchi 90s")
    generic_handler(
        "https://gaana.com/radio/mirchiplay-mirchi-90s",
        "mirchi_90s",
        "Mirchi Play Started...",
        visible,
    )
