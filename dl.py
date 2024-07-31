import requests

url = 'https://train-exo.s3.eu-west-1.amazonaws.com/2317/MovieReview.csv'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    with open('MovieReview.csv', 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")