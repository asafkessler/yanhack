import data_access_layer.mongodb_connection as mongo_clint
import utils.data_parser as parser
if __name__ == '__main__':
    mongo_clint.test(parser.parse_by_schema())