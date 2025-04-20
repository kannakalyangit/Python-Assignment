# config_parser.py

import configparser  # To read the .ini configuration file
import json          # To save the parsed data as JSON
from flask import Flask, jsonify  # To create the API

# Initialize Flask app
app = Flask(__name__)

# Parse the configuration file and store the data
parsed_data = {}

try:
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')  # This file contains the settings you want to parse

    # Loop through all sections in the configuration file and save them in parsed_data
    for section in config.sections():
        parsed_data[section] = dict(config.items(section))  # Convert each section into a dictionary

    # Save the parsed data to a JSON file for later use
    with open("output.json", "w") as json_file:
        json.dump(parsed_data, json_file, indent=4)  # Write JSON data with pretty indentation

except FileNotFoundError:
    print("❌ Configuration file not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")

# Create a simple GET API to serve the configuration data
@app.route('/config', methods=['GET'])
def get_config():
    """
    This API endpoint serves the parsed configuration data as JSON.
    """
    return jsonify(parsed_data)  # Flask will automatically convert the dictionary to JSON

if __name__ == '__main__':
    # Run the Flask web server
    app.run(debug=True)  # Running on localhost by default