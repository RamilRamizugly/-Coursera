import requests

token ='5e7529c75e7529c75e7529c7bf5e19d46c55e755e7529c703f0cf33dd30bc75e4f35500'
uid = 1234
def calc_age():
    r = requests.get('https://api.vk.com/method/users.get?user_ids=1234&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&v=5.101')
    print(r.text)


calc_age()



'''def main():

    r = requests.get('https://api.vk.com/method/users.get?user_ids=1')
    print(r)

main()'''