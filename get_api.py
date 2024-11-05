import requests

API_COMPLETED = 200

response = requests.get('https://api.fxratesapi.com/latest')

if response.status_code == API_COMPLETED:
    def get_response():
        return response
    
