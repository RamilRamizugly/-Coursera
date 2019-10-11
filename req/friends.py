
import requests
from datetime import datetime
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
    for item in search_dict['response']['items']:
        bdates = item.get('bdate')
        d = []
        try:
            for i in datetime.strptime(bdates, "%d.%m.%Y"):
                if i != None:
                    d = d.append(i)




        except TypeError:
            pass
        except ValueError:
            pass







calc_age()







