import json
import os
from begin.binance_interaction import query_binance_status, query_account


# Variable for the location of settings.json
import_filepath = "settings1.json"


# Function to import settings from settings.json
def get_project_settings(importFilepath):
    # Test the filepath to sure it exists
    if os.path.exists(importFilepath):
        # Open the file
        f = open(importFilepath, "r")
        # Get the information from file
        project_settings = json.load(f)
        # Close the file
        f.close()
        # Return project settings to program
        return project_settings
    else:
        return ImportError


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get the status
    status = query_binance_status()
    if status:
        print("Binance Ready To Go")

        # Import project settings
        project_settings = get_project_settings(import_filepath)
        print(project_settings)
        # Set the keys
        api_key = project_settings['BinanceKeys']['API_Key']
        secret_key = project_settings['BinanceKeys']['Secret_Key']
        # Retrieve account information
        account = query_account(api_key, secret_key)

        json_payload = json.dumps(account, indent=2)
        # print(opponents_json)
        if account['canTrade']:
            print("Let's Do This!")
            with open(f"output1.json", 'w', encoding='utf-8') as f:
                # f.write(json_payload.encode('ascii', 'ignore').decode('utf-8'))
                f.write(json_payload)

        else:
            print("Error!!!")
