from data_access_layer.models.track import Track
from data_access_layer.models.statevector import StateVector


def create_track_collection_from_db():
    tracks_map = {}

    def handle_track(track_from_db):
        state_v = StateVector()
        state_v.from_csv(track_from_db)

        if track_from_db["flight_id"] in tracks_map:
            track = tracks_map[track_from_db["flight_id"]]
        else:
            track = Track()
            track._id = track_from_db["flight_id"]

        track.add_to_state_vector_list(state_v)
        tracks_map[track.getId()] = track




