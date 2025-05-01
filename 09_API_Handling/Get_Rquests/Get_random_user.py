import requests


def fetch_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        username = data["data"]["login"]["username"]
        street_name = data["data"]["location"]["street"]["name"]
        return {"Username":username, "Streetname":street_name}
    else:
        raise Exception("Failed to fetch User Data!")
    

def main():
    try:
        lists = fetch_user_data()
        print(f"Username is {lists["Username"]} and Street Name is {lists["Streetname"]}")
    except Exception as e:
        print(str(e))
    


if __name__ == "__main__":
    main()
