import subprocess
from pathlib import Path 
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')




def get_dbt_models(project_dir, profiles_dir):
    try:
        # Use subprocess.run to execute the dbt ls command
        result = subprocess.run(['dbt', 'ls', '--project-dir', project_dir, '--profiles-dir', profiles_dir],
                                capture_output=True, text=True, check=True)

        # Check the output and extract model names
        if result.stdout:
            model_names = result.stdout.strip().split('\n')
            model_names = [model.split('.')[-1] for model in model_names]

            return model_names
        else:
            return []

    except subprocess.CalledProcessError as e:
        # If the command returns a non-zero exit code, handle the error
        return(f"Error running dbt ls: {e}")
        


