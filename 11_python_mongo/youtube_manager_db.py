from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://srikar:XuVSqvQnOnU9ibAd@cluster0.p60iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    print('*'*70)
    for video in video_collection.find({}):
        print(f"Id:{video['_id']}, Name:{video['name']}, Time:{video['time']}")
    print('*'*70)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(id, name, time):
    video_collection.update_one(
        {
            '_id': ObjectId(id)
        }, 
        {
            "$set": {"name": name, "time": time}
        }
    )    

def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})


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