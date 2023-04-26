import requests
import json

# JSON endpoint URL
url = "https://xyz.com/data.json"

# Make GET request to JSON endpoint
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Convert JSON response to Python dictionary
    data = json.loads(response.content)
    
    # Extract important data from dictionary and save to file
    important_data = data["important"]
    with open("important_data.txt", "w") as f:
        f.write(important_data)
        print("Important data saved to file")
else:
    print("Error: Request failed with status code", response.status_code)