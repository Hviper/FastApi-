import random
import requests
import hashlib
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=861163495@10.108.160.18; JSESSIONID=aaa6tFm-qtJc27dxCy_nx; OUTFOX_SEARCH_USER_ID_NCOO=140476714.59553656; ___rl__test__cookies=1595553248914'}
time1 = time.time()
sui = random.random()
bro = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
bv = hashlib.md5(bro.encode('utf-8')).hexdigest()
ts = int(time1 * 1000)
salt = str(ts) + str(int(sui * 10))
class Translate():

    def download(self,word):
        last = "fanyideskweb" + word + str(salt) + "mmbP%A-r6U3Nw(n]BjuEU"
        sign = hashlib.md5(last.encode('utf-8')).hexdigest()
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': bv,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        response = requests.post(url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule',headers=headers,data=data).json()
        dic=response["smartResult"]["entries"]
        print(response)
        return dic



print("sss\"")
# print()
# t = Translate()
#
# print("".join(t.download("word")))





