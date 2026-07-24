from requests_ip_rotator import ApiGateway
import requests

# Create gateway object and initialise in AWS
gateway = ApiGateway("https://checkip.amazonaws.com")
gateway.start()

# Assign gateway to session
session = requests.Session()
session.mount("https://checkip.amazonaws.com", gateway)

# Send request (IP will be randomised)
response = session.get("https://checkip.amazonaws.com", params={"theme": "light"})
print(response.text.rstrip())

# Delete gateways
gateway.shutdown()




