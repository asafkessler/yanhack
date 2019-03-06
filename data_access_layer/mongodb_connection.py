from data_access_layer.models.time import Time
from data_access_layer.models.flight import Flight
import json
from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://yanhack:yanhack123@yanhackdb-shard-00-00-g7qpy.azure.mongodb.net:27017,"
                     "yanhackdb-shard-00-01-g7qpy.azure.mongodb.net:27017,"
                     "yanhackdb-shard-00-02-g7qpy.azure.mongodb.net:27017/test?ssl=true&"
                     "replicaSet=YanhackDb-shard-0&authSource=admin&retryWrites=true")

flight_db_entity = client['flight_db']
flights_collection_entity = flight_db_entity['flights_collection']
small_flights_collection_entity = flight_db_entity['small_flights_collection']


def put_default_collection():
    flight_data = {
        'id': '3141',
        'content': 'checking if env is installed correctly',
        'author': 'Michael Ehrlich',
        'date': datetime.datetime.utcnow()
    }

    result = flights_collection_entity.insert_one(flight_data)
    print('One post: {0}'.format(result.acknowledged))


def put_basic_flights_collection(collection_name, json_data_frame):
    result = collection_name.insert_many(json_data_frame)
    print(result.acknowledged)


def get_all_dbs():
    return client.database_names()


def get_all_collections():
    collections_list = []
    for curr_db in client.database_names():
        collections_list.append(client[curr_db].collection_names())
    return collections_list


def retrieve_one_document(collection, key):
    """
    This method retrieves back one document, by its document key.
    :param collection: The db collection object.
    :param key: A dictionary of {"document_key": "search_value"}.
    For the first document just put empty dictionary {}.
    :return: Json Object.
    """
    one_json_document = collection.find_one(key)
    return one_json_document


def retrieve_many_documents(collection, document):
    """
      This method retrieves back many documents, by a document key.
      :param collection: The db collection object.
      :param document: A dictionary of {"document_key": "search_value"}.
      For all the collection just put empty dictionary {}.
      :return: Json List<Object>.
      """
    jsons_document = collection.find(document)
    return jsons_document


def delete_one_document(collection, document):
    """
      This method deletes one document, by its document key.
      :param collection: The db collection object.
      :param document: A dictionary of {"document_key": "search_value"}.
      For the first document just put empty dictionary {}.
      :return: Json List<Object>.
    """
    collection.delete_one(document)
    print(True)


def delete_many_documents(collection, document):
    """
     This method deletes many documents, by a document key.
     :param collection: The db collection object.
     :param document: A dictionary of {"document_key": "search_value"}.
     For all the collection just put empty dictionary {}.
     :return: Json List<Object>.
     """
    collection.delete_many(document)

def delete_number_of_documents(collection, number):
    # Offering us to delete from the Top By object id.
    # object_id = retrieve_one_document(collection, {})["_id"]
    # delete_one_document(collection, {"_id": object_id})
    document_number = number
    while document_number > 0:
        print("Deleting doc number:", document_number)
        delete_one_document(collection, {})
        document_number = document_number - 1


def retrieve_documents_in_range(collection, document_key, tuple_range):
    """
    Using IN Operators In mongodb.
    :return:
    """
    jsons_document = collection.find({document_key: {"$in": tuple_range}})
    return jsons_document


def retrieve_documents_under_roles(collection, document_keys, roles_list):
    """
    Using AND Operators In mongodb.
    :return:
    """
    cursor = collection.find({"status": "A", "qty": {"$lt": 30}})


def retrieve_documents_between_roles(collection, document_keys, roles_list):
    """
   Using OR Operators In mongodb.
   :return:
   """
    cursor = collection.find({"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]})


def retrieve_documents_under_and_between_roles(collection, document_keys, roles_list):
    cursor = collection.find({
        "status": "A",
        "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]})
