from pymongo import MongoClient

client = MongoClient("mongodb+srv://srikar:XuVSqvQnOnU9ibAd@cluster0.p60iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)


def main():
    pass

if __name__ == "__main__":
    main()