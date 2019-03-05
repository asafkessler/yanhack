import datetime

def utc_time_parser(time_string):
    """
    A method getting a utc time string and returning a time object.
    :param time_string: Utc time string.
    :return:Time object.
    """
    date_entity = datetime.datetime(time_string)
    # need to convert UTC time to Epoch
