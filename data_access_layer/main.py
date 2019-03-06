import data_access_layer.mongodb_connection as mongo_client
import utils.data_parser as parser
import utils.csv_files_handler as csv_handler

def db_main_information_compose():
    BASIC_FILE = "C:/flights_data/FlightAware_IAI_2015-01-01_2015-03-31_tracks.csv"
    print("size file:", csv_handler.file_size(BASIC_FILE))
    basic_data_frame = parser.create_flights_data_frame(BASIC_FILE)
    parser.print_file_attributes(basic_data_frame)
    half_gigabyte_flights_json = parser.create_half_gigabyte_db_collection(basic_data_frame)
    schema_based_flights_json = parser.create_schema_based_db_collection(basic_data_frame, half_gigabyte_flights_json)
    size_object = csv_handler.get_object_memory_size(schema_based_flights_json)
    print("size object :", size_object)
    mongo_client.put_basic_flights_collection(mongo_client.flight_db_entity, schema_based_flights_json)
    # OperationFailure: you are over your space quota, using 530 MB of 512 MB

if __name__ == '__main__':
    # Start of Presentation.
    print(csv_handler.get_relevant_file_path())





