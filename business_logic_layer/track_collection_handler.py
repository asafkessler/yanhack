from data_access_layer.models.track import Track
from data_access_layer.models.statevector import StateVector
import utils.csv_files_handler as csv_files_handler
import utils.data_parser as parser


def track_collection_create_in_db():
    file_path = csv_files_handler.get_relevant_file_path()
    tracks_data_frame = parser.create_flights_data_frame(file_path)
    tracks_json_frame = parser.create_small_tracks_db_collection(tracks_data_frame)
    track_map = create_track_collection_from_db(tracks_json_frame)
    return track_map


def create_track_collection_from_db(tracks_from_csv):
    tracks_map = {}

    for track_from_db in tracks_from_csv:
        state_v = StateVector()
        state_v.from_csv(track_from_db)

        if track_from_db["Flight ID"] in tracks_map:
            track = tracks_map[track_from_db["Flight ID"]]
        else:
            track = Track()
            track._id = track_from_db["Flight ID"]
            # track.csv_to_track(track_from_db)

        track.add_to_state_vector_list(state_v)
        tracks_map[track.getId()] = track

    return tracks_map


