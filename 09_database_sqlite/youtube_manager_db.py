import sqlite3

con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL,      
    )
''')

def list_all_videos():
    pass

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass

def main():
    while True:
        print('\n Youtbe Manager DB | Choose and option')
        print('1. list all youtube videos')
        print('2. add a video')
        print('3. update video details')
        print('4. delete a video')
        print('5. exit app')

        choice = input("enter your choice : ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input('enter video name : ')
                time = input('enter video duration : ')
                add_video(name, time)
            case '3':
                id = input('enter video id to update : ')
                name = input("enter video name : ")
                time = input("enter video time : ")
                update_video(id, name, time)
            case '4':
                id = input('enter video id to delete : ')
                delete_video(id)
            case '5':
                print('App Terminated !!!')
                break
            case _:
                print('Invalid Choice !!')

if __name__ == "__main__":
    main()