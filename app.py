from flask import Flask, jsonify, request
from dbt_python_methods.run_model import build_dwh_model
import logging
from pathlib import Path 

logging.basicConfig(level=logging.info, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

app = Flask(__name__)

@app.route('/')
def home():
    return 'dbt API is up and OK'


@app.route('/update_profiles_yml', methods=['GET'])
def update_profiles_yml():
    profile_details = request.get_json()
    
    server = request.get_json()['server']
    schema = request.get_json()['schema']
    username = request.get_json()['username']
    password = request.get_json()['password']


    
    try:
        created_profile = create_profiles_yaml(server, schema, username, password)
        return jsonify (created_profile), 201
    except Exception:
        return jsonify({'error while modifying profiles yml file': created_profile}), 400


    

@app.route('/run_model', methods=['GET'])
def run_model():
    
    project_dir = request.get_json()['project_name']
    model_name = request.get_json()['model_name']
    
    logging.info(f' Running dbt model {model_name} @project {project_dir}')
    try:
        model_run_log = run_dbt_model(model_name,project_dir)
        return jsonify(model_run_log), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400




@app.route('/run_all_models', methods=['GET'])
def run_all_models():
    
    project_name = request.get_json()['project_name']
    server = request.get_json()['server']
    port = request.get_json()['port']
    account_id = request.get_json()['account_id']
    username = request.get_json()['username']
    password = request.get_json()['password']
    
    
    #Example from dev env.
    # server = 'priority-erp-test.mysql.database.azure.com'
    # port = 3306
    # account_id = '03445d66'
    # username = 'erp_admin'
    # password = 'Wedding2104!'
    # project_name = 'priority_finance'
    # target = '03445d66'



    current_model = build_dwh_model(server,port,account_id,username,password,project_name)
    current_model.add_new_targets_to_profiles_yml()
    model_ls = current_model.get_dbt_models(project_name)


    for model_name in model_ls:
        fields_mapping = current_model.get_fields_mapping(model_name)
        current_model.run_dbt_model(model_name,project_name,fields_mapping,account_id)





    
    return jsonify('OK'), 200





# Run the app
if __name__ == '__main__':
    app.run(debug=True)


