from data_access_layer.models.track import Track
from data_access_layer.models.statevector import StateVector
import utils.csv_files_handler as csv_files_handler
import utils.data_parser as parser


def track_collection_create_in_db():
    file_path = csv_files_handler.get_relevant_file_path()
    tracks_csv = parser.create_csv_based_db_collection(file_path)
    t_map = create_track_collection_from_db(tracks_csv)
    t_map['bla']


def create_track_collection_from_db(tracks_csv):
    tracks_map = {}

    def handle_track(track_from_db):
        state_v = StateVector()
        state_v.from_csv(track_from_db)

        if track_from_db["flight_id"] in tracks_map:
            track = tracks_map[track_from_db["flight_id"]]
        else:
            track = Track()
            track._id = track_from_db["flight_id"]
            track.csv_to_track(track_from_db)

        track.add_to_state_vector_list(state_v)
        tracks_map[track.getId()] = track

    return tracks_map


