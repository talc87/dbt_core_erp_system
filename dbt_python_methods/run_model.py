import os
import subprocess
import yaml
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
import pymongo
import json
import certifi
connection_uri = "mongodb+srv://talcohen0507:Taltool87!@erpdataplatform.t8ot6ep.mongodb.net/"
ca_cert_path = certifi.where()






class build_dwh_model:
    
    def __init__(self,dwh_server,port,schema,username,password,project_name):

        self.dwh_server = dwh_server
        self.schema = schema
        self.username = username
        self.password = password
        self.port = port
        self.model_name=project_name
        
        #getting profiles.yml path
        current_folder_path = os.path.dirname(__file__)
        self.profiles_yml_path = os.path.dirname(current_folder_path) + '/' + project_name + '/profiles.yml'


    def get_fields_mapping(self,model_name):
        
        client = pymongo.MongoClient(connection_uri,tlsCAFile=certifi.where())
        
        db = client["admin_admin"]
        collection = db["field_mapping"]
        query = {"$and": [{"model": model_name}, {"account_id": self.schema}]}
        result = collection.find_one(query)

        mapping_json = dict(result)
        logging.debug('removing "_id" field')
        mapping_json.pop('_id',None)



        field_mapping = mapping_json
        logging.info(f'field mapping for account # {self.schema} model {model_name}\n {field_mapping}')
        return json.dumps(field_mapping)


    def add_new_targets_to_profiles_yml(self):
        logging.debug('getting profiles.yml path')
        current_folder_path = os.path.dirname(__file__)
        profiles_path = os.path.dirname(current_folder_path) + '/' + self.model_name + '/profiles.yml'

        
        logging.debug('Loading profiles.yml file')
        with open(profiles_path, 'r') as file:
            data = yaml.safe_load(file)

        logging.debug('Generating new target for the new client')
        new_profile = {

                self.schema: {

                    "outputs": {
                        "prod": {
                            "password": self.password,
                            "port": 3306,
                            "schema": self.schema,
                            "server": self.dwh_server,
                            "ssl_disabled": True,
                            "type": "mysql",
                            "username": self.username
                        }
                    },
                    "target": "prod"
                }
        }

        

        logging.debug(f"New profile's target which was generated \n{json.dumps(data, indent=4, sort_keys=True)}")
        data.update(new_profile)

        # Write back the modified data to the YAML file
        with open(profiles_path, 'w') as file:
            yaml.dump(data, file)



    
    
    def get_dbt_models(self,module_name):
        
        # Get the absolute path of the current script or module
        current_folder_path = os.path.dirname(__file__)

        # Get the path of the second parent folder (2 levels up)
        project_dir = os.path.dirname(current_folder_path) + '/'+module_name
        
        try:
            logging.debug(f'getting all models from project {project_dir}')
            command = ['dbt', 'ls', '--project-dir', project_dir,'--profiles-dir',project_dir]
            command_str = ' '.join(command)
            logging.debug(f'running command \n {command_str}')
            result = subprocess.run(command, capture_output=True, text=True)
            
            
            model_names = result.stdout.strip().split('\n')
            model_ls = [model.split('.')[-1] for model in model_names]
            logging.debug(f' the models found on the projects \n {model_ls}')

            return model_ls

        except subprocess.CalledProcessError as e:
            # If the command returns a non-zero exit code, handle the error
            return(f"Error getting dbt models list:\n {e}")





    def run_dbt_model(self,model_name,project_name,fields_mapping,target):
        # Get the absolute path of the current script or module
        current_folder_path = os.path.dirname(__file__)

        # Get the path of the second parent folder (2 levels up)
        project_dir = os.path.dirname(current_folder_path) + '/' + project_name
        logging.debug(f'dbt project dir is\n {project_dir}')

        command = [
                    'dbt', 'run',
                    '--select', model_name,
                    '--vars', fields_mapping,  
                    '--project-dir', project_dir,  
                    '--profiles-dir', project_dir,
                    '--profile' , target
                    ]


        # Create the command string with line breaks for printing
        command_str = ' '.join(command)

        # Print the command with line breaks
        logging.info(f'Running command:\n{command_str}')
        
        
        # Run the dbt model and creating the MySQL views
        try:
            dbt_run_results = subprocess.run(command)
            return {
                'model_name': model_name,
                'vars_mapping': fields_mapping,
                'dbt_cmd_command_string': ' '.join(dbt_run_results.args),
                'error_flag': dbt_run_results.stderr,
                'output': dbt_run_results.stdout
            }

        except Exception as e:
            raise Exception(f"An error occurred while running dbt model '{model_name}': {e}") from e












# server = 'priority-erp-test.mysql.database.azure.com'
# port = 3306
# account_id = '03445d66'
# username = 'erp_admin'
# password = 'Wedding2104!'
# project_name = 'priority_finance'
# target = '03445d66'



# current_model = build_dwh_model(server,port,account_id,username,password,project_name)
# current_model.add_new_targets_to_profiles_yml()
# model_ls = current_model.get_dbt_models(project_name)


# for model_name in model_ls:
#     fields_mapping = current_model.get_fields_mapping(model_name)
#     current_model.run_dbt_model(model_name,project_name,fields_mapping,account_id)



