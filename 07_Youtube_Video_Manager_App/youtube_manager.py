import json


def list_all_videos(videos):
    print('\n')
    print("*" * 80)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('\n')
    print("*" * 80)
    # print(index, video)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter a video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter a video name: ")
        time = input("Enter a video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid video number entered")


def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter a video number to be deleted: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Inavalid video number entered")


def load_videos():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)           


def main():
    videos = load_videos()
    while True:
        print("Youtube Manager | choose an option")
        print("1. List all favourite youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("Exit app successfully")
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()

