import pandas as pandas
import json
import data_access_layer.schemas.csv_columns_to_schema as schema_mapper


def create_flights_data_frame(file_path):
    """
    Core Method creates the data frame.
    :param file_path: chosen parsing file path.
    :return: data frame of the csv file.
    """
    flights_data_frame = pandas.read_csv(file_path)
    return flights_data_frame


def get_flights_json_data(flights_data_frame):
    """
    Core Method creates a json version of the information
    :param flights_data_frame:
    :return:
    """
    json_string = flights_data_frame.to_json(orient='records')
    data_frame_json = json.loads(json_string)
    return data_frame_json


def create_csv_based_db_collection(file_path):
    data_frame = create_flights_data_frame(file_path)
    json_frame = get_flights_json_data(data_frame)
    return json_frame


def create_schema_based_db_collection(flights_data_frame, general_json_frame):
    fixed_by_schema_json_frame = general_json_frame
    col = get_flight_columns(flights_data_frame)
    for flight in fixed_by_schema_json_frame:
        for index in range(len(col)):
            old_key = col[index]
            new_key = schema_mapper.mapper[old_key]
            flight[new_key] = flight.pop(old_key)
    return fixed_by_schema_json_frame


def create_half_gigabyte_db_collection(flights_data_frame):
    """
    That's half of the information in the first csv file, and returns it.
    :param file_path: default (first) parsing file path.
    :return: smaller json object.
    """
    basic_file_attributes = get_file_attributes(flights_data_frame)
    half_row_number = basic_file_attributes["row_count"] / 2

    # slicing the rows by half to get half gigabyte of data
    split_data_frame = flights_data_frame[0: int(half_row_number)]
    split_json_frame = get_flights_json_data(split_data_frame)
    return split_json_frame


def create_small_tracks_db_collection(flights_data_frame):
    """
    That's half of the information in the first csv file, and returns it.
    :param file_path: default (first) parsing file path.
    :return: smaller json object.
    """
    # slicing the rows by half to get half gigabyte of data
    small_tracks_json_frame = flights_data_frame[0: int(1000)]
    small_tracks_json_frame = get_flights_json_data(small_tracks_json_frame)
    return small_tracks_json_frame

def create_csv_information_head(flights_data_frame):
    """
    Experimenting with the data.
    :return: csv file with top 5 rows of the data frame.
    """
    flights_data_frame.head().to_csv("head.csv", index=False)


def print_file_attributes(data_frame):
    print("Rows Number : ", data_frame.shape[0], "Cols Number : ", data_frame.shape[1])


def get_file_attributes(data_frame):
    file_attributes = {"row_count": data_frame.shape[0],
                       "col_count": data_frame.shape[1]}
    return file_attributes


def print_data_information(flights_data_frame):
    print(flights_data_frame.info())
    print(flights_data_frame.corr())
    print(flights_data_frame.describe())


def get_flight_columns(flights_data_frame):
    return flights_data_frame.columns


"""
    Data Manipulation options:
    
    print(flights_data_frame.to_json(orient='columns'))
    print(flights_data_frame.to_json(orient='values'))
    print(flights_data_frame.to_json(orient='split', date_format='epoch'))
    print(flights_data_frame.columns)
"""
