import requests

# function to get user details from a free API
def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Name:", data["name"])
            print("Username:", data["username"])
            print("Email:", data["email"])
            print("City:", data["address"]["city"])
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    except Exception as e:
        print("Error:", e)

# call the function
get_user(1)
