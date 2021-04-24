from threading import Event
from zenlog import log
import signal
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys


track_list = []

browser = Chrome()
browser.maximize_window()


global ctrl_c_exit
ctrl_c_exit = Event()


def close_browser():
    global browser
    # browser.close()
    browser.quit()


def signal_handler(sig, frame):
    log.info("Saving songs information before quitting")

    with open("tracks.txt", "w") as f:
        f.write("Title\tAlbum/Artist(s)\n")
        for index in range(0, len(track_list)):
            f.write(
                "{}\t{}\n".format(
                    track_list[index]["title"], track_list[index]["artists_or_album"]
                )
            )
        f.close()

    close_browser()
    ctrl_c_exit.set()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
# signal.pause()

# import radio.trackinfo.trackinfo as tracks
# from radio.trackinfo.trackinfo import track_list

# from radio.radio import ctrl_c_exit


# from fake_useragent import UserAgent


def generic_handler(URL, station, default_title):
    global browser
    global track
    global track_list
    browser.get(URL)
    _title = None
    _artists_or_album = None

    try:
        # get the big play button and click
        big_play_button = browser.find_element_by_xpath("//a[@id='p-list-play_all']")
        big_play_button.click()
        log.debug("clicked on the play button")

        # sleeping for 3 senconds just to load everything properly (specially the track info),
        # depends on the network speed
        sleep(5)

        last_track_title = ""

        while not ctrl_c_exit.is_set():
            _title = browser.find_element_by_xpath("//h3[@id='stitle']").text
            _artists_or_album = browser.find_element_by_xpath("//p[@id='atitle']").text

            if _title == default_title:
                # skip station default audio ? IDN what is it called LOL :)
                continue

            # tracks.track.clear_info()

            if _title != last_track_title:
                # track.clear_info()
                # tracks.track.set_track_info(_title, _artists_or_album)
                # tracks.track.append_to_list()
                log.debug(
                    "Song => title: {}, artist(s)/album: {}".format(
                        _title, _artists_or_album
                    )
                )

                track_list.append(
                    {"title": _title, "artists_or_album": _artists_or_album}
                )
            # print(len(track_list))

            last_track_title = _title

            # checking for new track after every 2 minutes
            # TODO: other approach to see the chenges in track

            ctrl_c_exit.wait(30)

        # at this point we should close the browser
        close_browser()

    except Exception as e:
        log.critical(str(e))
        close_browser()
        sys.exit(0)


def pehla_nasha_handler():
    log.info("Starting radio mirchi pehla nasha")
    generic_handler("https://gaana.com/radio/mirchiplay-pehlanasha", "pehla_nasha")


def meethi_mirchi_handler():
    generic_handler(
        "https://gaana.com/radio/mirchiplay-meethi-mirchi",
        "meethi_mirchi",
        "Mirchi Play Started...",
    )
