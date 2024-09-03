import yaml
import json

path = '/Users/talcohen/Documents/Projects/dbt-MySQL/dbt_python_methods/profiles.yml'
# Load the YAML file
with open(path, 'r') as file:
    data = yaml.safe_load(file)

schema = 'account_id'
password = 'password_string'
dwh_server = 'db.server'
username = 'tal_username'

new_profile = {

        schema: {

            "outputs": {
                "prod": {
                    "password": password,
                    "port": 3306,
                    "schema": schema,
                    "server": dwh_server,
                    "ssl_disabled": True,
                    "type": "mysql",
                    "username": username
                }
            },
            "target": "prod"
        }
}

data.update(new_profile)
print(json.dumps(data, indent=4, sort_keys=True))



# Write back the modified data to the YAML file
with open(path, 'w') as file:
    yaml.dump(data, file)
