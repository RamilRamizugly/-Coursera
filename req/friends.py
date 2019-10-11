import requests
from datetime import datetime
from requests.exceptions import HTTPError

ID = input("Введите ID:")
token = 'e6c870a0e6c870a0e6c870a0e6e6a15244ee6c8e6c870a0ba496cb35b9f3a17905352b0'
API_VK = '5.71'
sleep = (3, 5)

URL_users = 'https://api.vk.com/method/users.get'
URL_friends = 'https://api.vk.com/method/friends.get'

base_payload = {'v': API_VK, 'access_token': token, 'timeout': sleep}


def get_id(user_ids):
    ids = []
    try:
        r1 = requests.get(URL_users,
                          params={**base_payload, **{'user_ids': ','.join(user_ids)}})
        data = r1.json()

        for i in range(len(user_ids)):
            ids.append(data['response'][i]['id'])

        r1.raise_for_status()
        return ids
    except HTTPError:
        print('HTTP error occurred')
    except Exception:
        print('Other error occurred')


def get_friends(user_id):
    user_id = get_id({user_id})[0]
    r1 = requests.get(URL_friends, params={
        **{'v': API_VK, 'access_token': token, 'fields': 'bdate', 'timeout': sleep},
        **{'user_id': user_id}})
    data = r1.json()
    friends_age = {}

    for i in range(data['response']['count']):
        row = data['response']['items'][i]
        if ('bdate' in row) and len(row['bdate'].split('.')) == 3:


            bdyear = int(row['bdate'].split('.')[2])
            age = datetime.now().year - bdyear
            friends_age[row['id']] = age

    return friends_age


def calc_age(user_id):
    friends_age = get_friends(user_id)
    age_friends = {}
    for k, v in friends_age.items():
        if v in age_friends:
            age_friends[v] += 1
        else:
            age_friends[v] = 1

    age_friends_list = list(age_friends.items())
    result1 = sorted(age_friends_list, key=lambda x: (-x[1], x[0])) # sorted sorted descending by second key (number of friends)
    #result2 = sorted(age_friends_list, key=lambda x: (-x[0], x[1])) # sorted ascending by first key (age)
    return result1


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
