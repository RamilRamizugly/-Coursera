from datetime import datetime
import requests
from datetime import datetime, date
import locale
locale.setlocale(locale.LC_ALL, "")
now = datetime.now()
today = datetime.today()

access_token = '5e7529c75e7529c75e7529c7bf5e19d46c55e755e7529c703f0cf33dd30bc75e4f35500'
api_version = '5.101'
token ='5e7529c75e7529c75e7529c7bf5e19d46c55e755e7529c703f0cf33dd30bc75e4f35500'
uid = 1234
def calc_age():
    r = requests.get('https://api.vk.com/method/friends.get?user_id=13586336&fields=bdate&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&v=5.101')
    search_dict = r.json()
    a=[]
    for item in search_dict['response']['items']:
        bdates = item.get('bdate')

        time_in_string = bdates
        time_in_datetime = datetime.strptime(time_in_string, "%d.%m.%Y").date()
        print(time_in_datetime)


        # print(bdates)
        # print(type(bdates))
        # print(len(str()))

        # try:
        #     list_iter = iter(bdates)
        #     for item in list_iter:
        #         if item is not None and item >= len(8):
        #             print(item)
        #         for _ in range(1):  # skip next 3 items
        #             next(list_iter, None)
        #             print(item)
        # except TypeError:
        #     print(item)


        # try:
        #     for i in datetime.strptime(bdates, "%d.%m.%Y"):
        #         if i is not None and i >= len(8):
        #             d = d.append(i)
        #             print(d)
        #         else:
        #             print(d)
        #
        #             list_iter = iter(item_list)
        #
        #
        #
        #                     do_something()






        # try:
        #
        #     for i in datetime.strptime(bdates, "%d.%m.%Y"):
        #         if i != None and i <= len(8):
        #             d = d.append(i)
        #             print(d)
        # except TypeError:
        #     continue
        # except ValueError:
        #     continue







calc_age()







