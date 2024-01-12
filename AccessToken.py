import requests
from requests.auth import HTTPBasicAuth

# Replace 'YOUR_CONSUMER_KEY' and 'YOUR_CONSUMER_SECRET' with your actual credentials
consumer_key = 'OCKQbxqNA2TtBEz3rAX511G0MtpM5WBu'
consumer_secret = 'jnC1NkF7ocYEcWb4'

# URL for Safaricom API
access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

# Prepare headers
headers = {
    'Content-Type': 'application/json; charset=utf8',
}

# Prepare authentication
auth = HTTPBasicAuth(consumer_key, consumer_secret)

# Make a request to Safaricom API
response = requests.get(access_token_url, headers=headers, auth=auth)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract and print the access token
    access_token = data.get('access_token')
    print(access_token)
else:
    # Print an error message if the request was not successful
    print('Failed to get access token')
