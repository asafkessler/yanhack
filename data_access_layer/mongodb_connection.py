import datetime
from pymongo import MongoClient
import data_access_layer.consts_db as DBConst

client = MongoClient(DBConst.CONNECTION_STRING)

flight_db_entity = client[DBConst.FLIGHT_COLLECTION_NAME]
flights_collection_entity = flight_db_entity[DBConst.FLIGHT_DB_ENTITY_NAME]


def put_default_collection():
    flight_data = {
        'id': '3141',
        'content': 'checking if env is installed correctly',
        'author': 'Michael Ehrlich',
        'date': datetime.datetime.utcnow()
    }

    result = flights_collection_entity.insert_one(flight_data)
    print('One post: {0}'.format(result.acknowledged))


def put_basic_flights_collection(json_data_frame):
    result = flights_collection_entity.insert_many(json_data_frame)
    print(result.acknowledged)


def get_all_dbs():
    return client.database_names()


def get_all_collections():
    collections_list = []
    for curr_db in client.database_names():
        collections_list.append(client[curr_db].collection_names())
    return collections_list


def retrieve_one(collection):
    bills_post = collection.find_one({'author': 'Bill'})
    print(bills_post)


def retrieve_many(collection):
    scotts_posts = collection.find({'author': 'Scott'})
    print(scotts_posts)
