import os
import requests
from flask import Blueprint, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

balancing_authorities_blueprint = Blueprint('balancing_authorities', __name__)

@balancing_authorities_blueprint.route('/api/balancing_authorities', methods=['GET'])
def get_balancing_authorities():
    
    # Load the API key from the environment variable
    api_key = os.getenv('EIA_API_KEY')
    
    if not api_key:
        return jsonify({"error": "API key not found."}), 500
    
    url = "https://api.eia.gov/v2/electricity/rto/region-data/data/"
    params = {
        "api_key": api_key,
        "frequency": "hourly",
        "length": 5000,
        "offset": 0# Start at the first record
    }

    # Initialize a set to store unique balancing authorities
    balancing_authorities = set()

    while True:
        # Make the GET request to the API
        response = requests.get(url, params=params)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()

            # Check if 'data' is in the response and iterate over i
            if'response'in data and'data'in data['response']:
                    records = data['response']['data']
                    if not records:  # Break the loop if no more records
                      break
                    # Extract balancing authorities and add them to the set
                    for record in records:
                        ba = record.get('respondent')
                        if ba:
                            balancing_authorities.add(ba)
                    
                    # Increment the offset for the next batch of records
                    params['offset'] += len(records)
            else:
              break
        else:
          return jsonify({"error": f"Failed to fetch data. Status code: {response.status_code}"}), 500
        
        # Convert the set to a sorted list and return as JSON
        return jsonify(sorted(balancing_authorities))
