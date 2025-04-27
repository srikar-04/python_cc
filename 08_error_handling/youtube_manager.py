import json
# there are two operations using json
# dump -> converting "python object to json string"
# load -> converting "json string to python object"

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            loaded_data = json.load(file)
            print(f"loaded data -> {loaded_data} \n loaded data type -> {type (loaded_data)}")
            return loaded_data
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        # print('dumping the list into the file in save_data_helper : ', json.dump(videos, file))
        dumped_data = json.dump(videos, file)
        print(f"dumped data -> {dumped_data} \n dumped data type -> {type (dumped_data)}")


def list_all_videos(videos):
    print('*' * 70, '\n')
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")
    print('\n', '*' * 70)

def add_video(videos):
    name = input('enter video name : ')
    time = input('enter video time : ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter video number to update : '))
    if 1 <= index <= len(videos):
        name = input('Enter new video name : ')
        time = input('Enter new video time : ')
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print('Invalid index selected !!!')

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter video number to delete : '))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid video index deleted !!!')


def main():
    videos = load_data()
    while True:
        print('\n Youtbe Manager | Choose and option')
        print('1. list all youtube videos')
        print('2. add a video')
        print('3. update video details')
        print('4. delete a video')
        print('5. exit app')

        choice = input('Enter your choice : ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print('App Terminated !!!')
                break
            case _:
                print('Invalid Choice !!')

if __name__ == '__main__':
    main()