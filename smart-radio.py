import argparse
import signal
import sys

from zenlog import log


class Stations:
    def __init__(self):
        self.entries = [
            {"id": "pehla_nasha", "handler": "gaana"},
            {"id": "meethi_mirchi", "handler": "gaana"},
            {"id": "english_love", "handler": "gaana"},
            {"id": "rabindra_sangeet", "handler": "gaana"},
            {"id": "toota_dil", "handler": "gaana"},
            {"id": "filmy_mirchi", "handler": "gaana"},
            {"id": "international_hits", "handler": "gaana"},
            {"id": "english_retro_hits", "handler": "gaana"},
            {"id": "mirchi_90s", "handler": "gaana"},
        ]

    def is_valid(self, _id):
        for index in range(0, len(self.entries)):
            if self.entries[index]["id"] == _id:
                return index
        return False

    def get_handler(self, _id):
        index = self.is_valid(_id)
        if index is not False:
            return self.entries[index]["handler"]
        return None


stations = Stations()

parser = argparse.ArgumentParser(
    description="Play radio from the CLI and save songs information to check them later",
    prog="SMART-RADIO",
)

parser.add_argument("--version", action="version", version="%(prog)s 1.0")

parser.add_argument(
    "--station",
    action="store",
    dest="station_name",
    help="Specify a station name",
)

parser.add_argument(
    "--visible",
    action="store_true",
    default=False,
    dest="visible",
    help="Make the browser window visible",
)
parser.add_argument(
    "--log-level",
    action="store",
    default="info",
    dest="log_level",
    help="Specify log level",
)

results = parser.parse_args()

log_level = results.log_level
if log_level in ["info", "error", "debug"]:
    log.level(log_level)
else:
    log.level("info")
    log.warning("Correct log levels are: error,warning,info(default),debug")

station_id = None
station_id = results.station_name

if station_id is None:
    log.critical("Need a station name to play the radio, see help")
    sys.exit(0)

log.debug("Station id: " + station_id)
log.debug("Visibility: " + str(results.visible))


handler = stations.get_handler(station_id)
if handler is None:
    log.critical("{} is not a valid station name".format(station_id))
    sys.exit(0)

if handler == "gaana":
    from radio.radio import Gaana, gaana

    target_station = Gaana.__getattribute__(gaana, station_id)
    target_station(results.visible)
