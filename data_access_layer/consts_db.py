# connection string (to mongo)
CONNECTION_STRING = ("mongodb://yanhack:yanhack123@yanhackdb-shard-00-00-g7qpy.azure.mongodb.net:27017," +
                     "yanhackdb-shard-00-01-g7qpy.azure.mongodb.net:27017," +
                     "yanhackdb-shard-00-02-g7qpy.azure.mongodb.net:27017/test?ssl=true&" +
                     "replicaSet=YanhackDb-shard-0&authSource=admin&retryWrites=true")


# db name
FLIGHT_COLLECTION_NAME = 'flight_db'

# collection names
FLIGHT_DB_ENTITY_NAME = 'flights_collection'
TRACKS_DB_ENTITY_NAME = 'tracks_collection'

