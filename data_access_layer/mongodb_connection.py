from pymongo import MongoClient

client = MongoClient("mongodb://yanhack:<yanhack123>@yanhackdb-shard-00-00-g7qpy.azure.mongodb.net:27017,"
                     "yanhackdb-shard-00-01-g7qpy.azure.mongodb.net:27017,"
                     "yanhackdb-shard-00-02-g7qpy.azure.mongodb.net:27017/test?ssl=true&"
                     "replicaSet=YanhackDb-shard-0&authSource=admin&retryWrites=true")
db = client.test
