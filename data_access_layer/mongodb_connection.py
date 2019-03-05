from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://yanhack:yanhack123@yanhackdb-shard-00-00-g7qpy.azure.mongodb.net:27017,"
                     "yanhackdb-shard-00-01-g7qpy.azure.mongodb.net:27017,"
                     "yanhackdb-shard-00-02-g7qpy.azure.mongodb.net:27017/test?ssl=true&"
                     "replicaSet=YanhackDb-shard-0&authSource=admin&retryWrites=true")

flight_db_entity = client['flight_db']
flights_collection_entity = flight_db_entity['flights_collection']

flight_data = {
    'id': '3141',
    'content': 'checking if env is installed correctly',
    'author': 'Michael Ehrlich',
    'date': datetime.datetime.utcnow()
}
result = flights_collection_entity.insert_one(flight_data)
print('One post: {0}'.format(result.acknowledged))

def put_df(df):
    client['mainDb']['flights'].insert_many(df.to_dict())