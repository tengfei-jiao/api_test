import requests
from libs.model_001 import *
from libs.model_002 import *

#
# # 配置环境的sesion,token
# huanjing = [1, 2, 3]
# def gen_session():
#     if huanjing == 1:
#         return "token1"
#     elif huanjing ==2:
#         return "token2"
#     elif huanjing == 3:
#         return "token3"


def get_cookie():
    url = "https://mubu.com/api/login/submit"
    headers = {"User-Agent": "HttpRunner"}
    body = {"phone": "18710748230", "password": "123456", "remember": "true"}
    res = requests.post(url, headers=headers, data=body)
    # return res.cookies["SESSION"]
    print("这里是token:", res.cookies["Jwt-Token"])
    print("这里是session:", res.cookies["SESSION"])
    print("这里是cookie:", res.cookies)
    print("这里是headers中的cookies:", res.headers["Set-Cookie"])


if __name__ == '__main__':
    get_cookie()

