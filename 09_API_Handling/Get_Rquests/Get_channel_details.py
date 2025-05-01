import requests


def Get_channel_details():
    url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    response = requests.get(url)
    data  = response.json()

    if data["success"] and "data" in data:
        title = data["data"]["info"]["snippet"]["localized"]["title"]
        description = data["data"]["info"]["brandingSettings"]["channel"]["description"]
        return [title, description]
    else:
        raise Exception("Failed to fetch channel information!")
    


def main():
    try:
        lists = Get_channel_details()
        print(f"Channel Title is: {lists[0]} \n\n Video description is {lists[1]}")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()