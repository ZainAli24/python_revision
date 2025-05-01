import requests

def fetch_userData_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)  
    data = response.json()
    # print(type(data))

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data!")
    

def main():
    try:
        username, country = fetch_userData_from_freeapi()
        print(f"Username is : {username} \nCountry is : {country}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()


# ---------------------------------------------
# 2. return dictionary: 
def fetch_userData_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)  
    data = response.json()
    # print(type(data))

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return {'username': username , 'country': country}   # return dictionary
    else:
        raise Exception("Failed to fetch user data!")
    

def main():
    try:
        user_list = fetch_userData_from_freeapi()
        print("user dictionary: ",user_list['username'],",", user_list['country'])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()




# ---------------------------------------------
# 3. return list: 
def fetch_userData_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)  
    data = response.json()
    # print(type(data))

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return [username , country]  # return list
    else:
        raise Exception("Failed to fetch user data!")
    

def main():
    try:
        user_list = fetch_userData_from_freeapi()
        print("user list: ",user_list[0],",", user_list[1])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

