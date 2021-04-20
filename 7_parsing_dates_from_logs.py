# In this bite we will look at this small server log finding the first and last
# system shutdown events:
#
# INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
# ...
# INFO 2014-07-03T23:31:22 supybot Shutdown initiated.

# You need to calculate the time between these two events. First extract the
# timestamps from the log entries and convert them to datetime objects. Then
# use datetime.timedelta to calculate the time difference between them.
#
# You can assume the logs are sorted in ascending order. Check out the
# docstrings and the TESTS for more info.

from datetime import datetime
import os
import re
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    """
    Extract timestamp from logline and convert it to a datetime object.
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns:
    datetime(2014, 7, 3, 23, 27, 51)
    """
    time_components = re.findall(r"\d+", line)
    timestamp = [int(component) for component in time_components]
    return datetime(*timestamp)


def time_between_shutdowns(loglines):
    """
    Extract shutdown events ("Shutdown initiated") from loglines and
    calculate the timedelta between the first and last one.
    Return this datetime.timedelta object.
    """
    shutdown_events = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            shutdown_events.append(convert_to_datetime(line))
    return shutdown_events[1] - shutdown_events[0]


if __name__ == "__main__":
    print(time_between_shutdowns(loglines))
