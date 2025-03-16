1. CREATE table Command:

CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);


2. SELECT all data from videos table:
cursor.execute("SELECT * FROM videos")
rows = cursor.fetchall()


3. ADD values in (name and time fields) of the videos table :
cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
conn.commit()


4. Update values in (name and time fields) of the videos table :
cursor.execute("UPDATE videos SET name= ?, time= ? WHERE id = ?", (name, time, video_id))
conn.commit()


5. DELETE row from videos table :
cursor.execute("DELETE FROM videos where id = ?", (video_id,))
conn.commit()
