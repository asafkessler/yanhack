import pandas as pandas
import json
import data_access_layer.schemas.csv_columns_to_schema as schema_mapper

DATA_PREFIX_PATH = "C:\\flights_data\\"
flights_data_paths = [DATA_PREFIX_PATH + "FlightAware_IAI_2015-01-01_2015-03-31_tracks.csv",
                      DATA_PREFIX_PATH + "FlightAware_IAI_2015-04-01_2015-06-30_tracks.csv",
                      DATA_PREFIX_PATH + "FlightAware_IAI_2015-07-01_2015-09-30_tracks.csv",
                      DATA_PREFIX_PATH + "FlightAware_IAI_2015-10-01_2015-12-31_tracks.csv"]

flights_data_frame = pandas.read_csv("C:/devl/Work/asaf-python-projects/yanhack/utils/head.csv",
                                     low_memory=False)

"""
    Experimenting with the data.
"""
# print(flights_data_frame.head().to_csv("head.csv", index=False))
# print(flights_data_frame.info())
# print(flights_data_frame.corr())
# print(flights_data_frame.describe())


# def get_flight_map_elem_by_index(index):
#     json_string = flights_data_frame.to_json(orient='index')
#     data_frame_json = json.loads(json_string)


def get_flight_columns():
    return flights_data_frame.columns

# print(flights_data_frame.to_json(orient='columns'))
# print(flights_data_frame.to_json(orient='values'))
# print(flights_data_frame.to_json(orient='split', date_format='epoch'))
# print(flights_data_frame.columns)

def get_flights_json_data():
    json_string = flights_data_frame.to_json(orient='records')
    data_frame_json = json.loads(json_string)
    return data_frame_json

def parse_by_schema():
    data = get_flights_json_data()
    col = get_flight_columns()
    for flight in data:
        for index in range(len(col)):
            old_key = col[index]
            new_key = schema_mapper.mapper[old_key]
            flight[new_key] = flight.pop(old_key)
    return data