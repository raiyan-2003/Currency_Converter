import requests

API_COMPLETED = 200  # .status code sends 200 constant in order to signal completion

response = requests.get('https://api.fxratesapi.com/latest')

if response.status_code == API_COMPLETED:
    def get_response():
        return response
    
