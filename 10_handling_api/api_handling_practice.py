import requests
import random
import math

def get_joke_by_id(joke_id):
    url = f"https://api.freeapi.app/api/v1/public/randomjokes/{joke_id}"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        return data["data"]['content']
    else:
        raise Exception('Failed to fetch joke !!!!')
    
def random_number():
    random_num = math.floor((random.random()*1000) + 1)
    print("random number : ", random_num)
    return random_num


def main():
    try:
        joke = get_joke_by_id(random_number())
        print(joke)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()