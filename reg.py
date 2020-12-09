import requests
import string
import random
import os
from time import sleep


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_cookie(user,pwd):
    headers = {
    'authority': 'mbasic.facebook.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://mbasic.facebook.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-J600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'vi',
    }

    params = (
        ('lwv', '100'),
        ('refid', '8'),
    )

    data = {
      'try_number': '0',
      'unrecognized_tries': '0',
      'email': user,
      'pass': pwd,
      'login': '\u0110\u0103ng nh\u1EADp'
    }
    session = requests.session()
    response = session.post('https://mbasic.facebook.com/login/device-based/regular/login/', headers=headers, params=params, data=data)
    x = session.cookies
    c_user = x['c_user']
    datr = x['datr']
    fr = x['fr']
    sb = x['sb']
    xs = x['xs']
    ck = f'sb={sb}; datr={datr}; c_user={c_user}; xs={xs}; fr={fr}'
    print(ck)
    f = open('cookie.txt', 'a')
    f.write(f'{ck}\n')
    f.close()

def reg():
    user = f'{get_random_string(random.choice(range(5,10)))}@gmail.com'
    headers = {
        'authority': 'b-api.facebook.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cookie': '_fbp=fb.1.1589291794927.1734409733; sb=YnQkX279Q2vDSFwoWr-2_Cu_; datr=ZXQkX2szSC58Ul_I0Bexek6b; c_user=100006177545047; spin=r.1002626428_b.trunk_t.1599302211_s.1_v.2_; cppo=1; xs=33%3Afq6jfw3MdmC8IQ%3A2%3A1597762608%3A11215%3A6327%3A%3AAcUiH8eWMjoODFDW4EjzFHOZ6Mnh5zTpcW1zCgW7RSCK; fr=1V5t18xNcveHIKBZa.AWWrEwr6jrogXbXjUnofazG-Aks.BfJHRi.BA.F9R.0.0.BfVAej.AWU6Q9NW; presence=EDvF3EtimeF1599344919EuserFA21B06177545047A2EstateFDsb2F1599338411532EatF1599338484136Et3F_5bDiFA2user_3a1B05345028811A2EoF1EfF2CAcDiFA2thread_3a1900876286638988A2EoF2EfF1C_5dEutc3F1599338410715G599338484148CEchF_7bCC; wd=1366x657',
    }

    params = (
        ('attempt_login', 'true'),
        ('birthday', '1990-09-08'),
        ('client_country_code', 'VN'),
        ('firstname', 'Tien'),
        ('lastname', 'Nhat'),
        ('gender', 'F'),
        ('email', user),
        ('locale', 'vi_VN'),
        ('password', 'tunglg12'),
        ('return_multiple_errors', 'true'),
        ('format', 'json'),
        ('access_token', '350685531728|62f8ce9f74b12f84c123cc23437a4a32'),
    )

    response = requests.get('https://b-api.facebook.com/method/user.register', headers=headers, params=params)
    a = response.json()
    if a['error_code'] == 407:
      print(f'{user}|tunglg12')


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://b-api.facebook.com/method/user.register?attempt_login=true&birthday=1990-09-09&client_country_code=VN&firstname=Tien&lastname=Nhat&gender=F&email=starnhatmaxilx.newnew@gmail.com&locale=vi_VN&password=starnhat123&return_multiple_errors=true&format=json&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32', headers=headers)


for x in range(1,10000):
  reg()
  sleep(30)
