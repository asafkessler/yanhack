mapper = {"Flight ID": "flight_id",
          "Ident": "identification",
          "Type": "type",
          "Origin": "origin",
          "Destination": "destination",
          "Time (UTC)": "time",
          "Latitude": "latitude",
          "Longitude": "longitude",
          "Groundspeed (kts)": "ground_speed",
          "Altitude (ft)": "altitude",
          "Rate": "rate",
          "Course": "course",
          "Direction": "direction",
          "Facility Name": "facility_name",
          "Facility Description": "facility_description",
          "Estimated Pos.": "estimated_position"
          }

track_mapper = [
    "Ident",
    "Type",
    "Origin",
    "Destination",
    "Facility Name",
    "Estimated Pos.",
    "Facility Description"
]

# import json
# class CSV_Columns_To_Schema:
#     reletive_path
#     with open("schemas/flight_schema.json") as message_schema:
#         print(message_schema)
