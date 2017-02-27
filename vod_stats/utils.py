import dateutil.parser
import calendar


def get_timestamp_from_str(date_str):
    return calendar.timegm(dateutil.parser.parse(date_str).utctimetuple())
