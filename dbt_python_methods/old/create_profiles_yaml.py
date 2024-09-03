import yaml
import io
import os
import logging
import json
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def add_profile(self, target_type = 'mysql',port=3306,ssl_disabled=True):
    
    target_name = 'prod_'+{self.schema}
    
    new_profile = {
                self.schema: {
                    'target': target_name,
                    'outputs': {
                        'prod': {
                            'type': target_type,
                            'server': self.dwh_server,
                            'port': port,
                            'schema': self.schema,
                            'username': self.username,
                            'password': self.password,
                            'ssl_disabled': ssl_disabled
                        }
                    }
                }
            }

    

    # Get the absolute path of the current script or module
    current_file_path = os.path.abspath(__file__)

    # Get the path of the parent folder (folder above the current file)
    parent_folder_path = os.path.dirname(os.path.dirname(current_file_path))

    profile_path = =parent_folder_path + '/{}+/'
    # Now 'parent_folder_path' contains the path of the folder above the current file
    print("Parent Folder Path:", parent_folder_path)











    

'''

    # Get current file path
    current_file_path = os.path.abspath(__file__)
    # Get the parent directory of the file
    #parent_dir = os.path.pardir(current_path)
    # Construct the output file path
    #target_path = os.path.join(parent_dir, 'priority_finance', 'profiles.yml')
    #logging.info(f'profiles.yaml will be saved at {target_path}')
    parent_folder = os.path.dirname(current_file_path)

    logging.debug('Read the existing dbt profile.yml file')
    with open('profiles.yml', 'r') as file:
        dbt_profile = yaml.safe_load(file)



    logging.debug('Add the new profile to the existing profile.yml')
    dbt_profile['profiles'].update(new_profile)

    logging.debug('Write the updated profiles.yml back to the file')
    with open('profiles.yml', 'w') as file:
        yaml.dump(dbt_profile, file)


    try:
        with open(target_path, 'w') as yaml_file:
            yaml_profile = yaml.safe_dump(data, yaml_file)
        logging.info(f'Retriving profiles.yml')
        # Read YAML data from file
        with open(target_path, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
        return yaml_data
        
        
    except (FileNotFoundError, PermissionError) as e:
        logging.error(f"Error occurred while writing YAML: {e}")
        return e
    
    

'''



# Usage example
account_id = '02721d99'
target = 'dev'
server = 'localhost'
schema = account_id
username = 'root'
password = 'Taltool87!'
ssl_disabled = True

x = add_profile(server, schema, username, password)
print(x)

