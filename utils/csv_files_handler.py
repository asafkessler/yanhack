import tkinter as window_tool
from tkinter import filedialog
import os
import sys


def get_object_memory_size(obj):
    return convert_bytes(sys.getsizeof(obj))


def get_half_gb_information_from_file(file_path):
    pass


def get_relevant_file_path():
    root_window = window_tool.Tk()
    root_window.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def create_default_files_path_list():
    # DATA_PREFIX_PATH = "C:/flights_data/"
    DATA_PREFIX_PATH = os.environ['FLIGHTS_DATA']
    flights_data_paths = [DATA_PREFIX_PATH + "FlightAware_IAI_2015-01-01_2015-03-31_tracks.csv",
                          DATA_PREFIX_PATH + "FlightAware_IAI_2015-04-01_2015-06-30_tracks.csv",
                          DATA_PREFIX_PATH + "FlightAware_IAI_2015-07-01_2015-09-30_tracks.csv",
                          DATA_PREFIX_PATH + "FlightAware_IAI_2015-10-01_2015-12-31_tracks.csv"]
    return flights_data_paths


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
