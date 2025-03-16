import sqlite3


conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
)
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    print("-" * 80)
    if not rows:
        print("List is empty, Please Add vidoes")
    else:
        for row in rows:
            # print('. '.join(str(item) for item in row))
            print(f"{row[0]}. {row[1]}, Duration: {row[2]}")
    print("-" * 80)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_vidoe(name, time, video_id):
    cursor.execute("UPDATE videos SET name= ?, time= ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("Youtube Video Manager App with sql-DB")
        print("1. list All videos")
        print("2. Add video")
        print("3. Update video")
        print("4. delete video")
        print("5. Exit app")
        choice = input("Enter Your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)

            case '3':
                list_all_videos()
                video_id = input("Enter video id to update: ")
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_vidoe(name, time, video_id)
            case '4':
                list_all_videos()
                video_id = input("Enter video id to be deleted: ")
                delete_video(video_id)
            case '5':
                print("Exit app sucessfully")
                break
            case _:
                print("Invalid Choice entered!")
    conn.close()





if __name__ == "__main__":
    main()
