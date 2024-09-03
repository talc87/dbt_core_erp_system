import logging
import pymongo


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

connection_uri = "mongodb+srv://talcohen0507:Taltool87!@erpdataplatform.t8ot6ep.mongodb.net/"

def get_field_mapping(account_id,model):
    client = pymongo.MongoClient(connection_uri)
    db = client["admin_admin"]
    collection = db["field_mapping"]
    query = {"$and": [{"model": model}, {"account_id": account_id}]}
    result = collection.find_one(query)


    mapping_json = dict(result)
    logging.debug('removing "_id" field')
    mapping_json.pop('_id',None)
    field_mapping = mapping_json
    logging.info(f'field mapping for account # {account_id} model {model}\n {field_mapping}')



account_id = '03445d66'
model = 'dim_accounts'

get_field_mapping(account_id,model)
