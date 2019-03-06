import datetime


def UTC_time_to_epoch(timestamp):
    """
      A method getting a utc time string and returning a time object.
      :param timestamp:Utc time string.
      :return:long.
      # ex. 01/01/2015 13:08:48
    """
    unix_epoch = datetime.datetime(1970, 1, 1)
    log_dt = datetime.datetime.strptime(timestamp, "%Y/%m/%d %H:%M:%S")
    miliseconds_from_epoch = (log_dt - unix_epoch).total_seconds() * 1000
    return miliseconds_from_epoch

