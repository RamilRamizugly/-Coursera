import requests
import pydash


access_token = '5e7529c75e7529c75e7529c7bf5e19d46c55e755e7529c703f0cf33dd30bc75e4f35500'
api_version = '5.101'
token ='5e7529c75e7529c75e7529c7bf5e19d46c55e755e7529c703f0cf33dd30bc75e4f35500'
uid = 1234
def calc_age():
    r = requests.get('https://api.vk.com/method/friends.get?user_id=13586336&fields=bdate&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&v=5.101')
    search_dict = r.json()
    response_key = search_dict.get('response')
    items_key = response_key.get('items')


    #list_dikt= items_key[1]
    iter_item = iter(items_key)
    print(next(iter_item,None))


    #print(list_dikt)
    #print(type(list_dikt))


calc_age()







