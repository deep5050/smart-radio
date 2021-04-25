import sys
import signal
import argparse
from zenlog import log

from radio.stations.stations import Stations

stations = Stations()

station_id = None
log_level = None

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
    log.debug("Importing gaana handler")
    from radio.radio import gaana, Gaana

    target_station = Gaana.__getattribute__(gaana, station_id)
    target_station(results.visible)