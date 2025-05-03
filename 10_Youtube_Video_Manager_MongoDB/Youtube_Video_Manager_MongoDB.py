# 1. First way :
# import pymongo

# client = pymongo.MongoClient("mongodb+srv://zain:sameer@cluster0forlearning.rprbrnq.mongodb.net/ytmanager")
# Not a Good idea to inclide id and password in the code. Use environment variables or a config file.

# 2. Second way:
from pymongo import MongoClient
from bson.objectid import ObjectId # bson json ka bara bhai hai.

client = MongoClient("mongodb+srv://zain:sameer@cluster0forlearning.rprbrnq.mongodb.net/")

db = client["ytmanager"] # Database name
videos_collection = db["videos"] # Collection name
print(videos_collection)  # Confirming the connection to the collection

# client.close() # to close your connection from MongoDB.



def view_all_videos():
    for video in videos_collection.find():
        # id = str(video["_id"])
        # ids = id[-2:]
        print(f"ID: {video["_id"]}, Name: {video["name"]} and Time: {video["time"]}")

def add_new_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    videos_collection.update_one(
        {"_id": ObjectId(video_id)}, # is mien wo ata hai jis ko update karna hai.
        {"$set": {"name":name, "time":time}}  # is mien hum btate hai ke kia operation lgana hai update wale par.
    )

def delete_video(video_id):
    videos_collection.delete_one({"_id":ObjectId(video_id)})



def main():
    while True:
        print("Welcome to the Youtube Video Manager")
        print("1. View all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the App")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                view_all_videos()

            case "2":
                name= input("Enter the name of the video: ")
                time= input("Enter the time of the video: ")
                add_new_video(name, time)

            case "3":
                video_id= input("Enter the id of the video to update: ")
                name= input("Enter the name of the video to update: ")
                time= input("Enter the time of the video to update: ")
                update_video(video_id, name, time)


            case "4":   
                video_id_del= input("Enter the id of the video to delete: ")
                delete_video(video_id_del)

            case "5":
                print("Exiting the app Successfully...")
                break
            case _:
                print("Invalid choice. Please try again.")  


if __name__ == "__main__":
    main()


