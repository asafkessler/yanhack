import data_access_layer.mongodb_connection as mongo_clint
import utils.data_parser as parser
import utils.csv_files_handler as csv_handler
import business_logic_layer.track_collection_handler as track_handler
from data_access_layer.models.track import Track
import json

def push_data():
    BASIC_FILE = "C:/flights_data/FlightAware_IAI_2015-01-01_2015-03-31_tracks.csv"
    print("size file:", csv_handler.file_size(BASIC_FILE))
    basic_data_frame = parser.create_flights_data_frame(BASIC_FILE)
    parser.print_file_attributes(basic_data_frame)
    half_gigabyte_flights_json = parser.create_half_gigabyte_db_collection(basic_data_frame)
    schema_based_flights_json = parser.create_schema_based_db_collection(basic_data_frame, half_gigabyte_flights_json)
    size_object = csv_handler.get_object_memory_size(schema_based_flights_json)
    print("size object :", size_object)
    mongo_clint.put_basic_flights_collection(schema_based_flights_json)
    # OperationFailure: you are over your space quota, using 530 MB of 512 MB

if __name__ == '__main__':
    tracks_map = track_handler.track_collection_create_in_db()
    list_of_values = []
    for key in tracks_map.keys():
        list_of_values.append(json.dumps(tracks_map[key]))
    print(json.dumps(tracks_map))
    #mongo_clint.put_basic_flights_collection(mongo_clint.fixed_flights_collection_entity, list_of_values)


