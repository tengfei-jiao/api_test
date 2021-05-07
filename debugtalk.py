import requests
import os, time
from bs4 import BeautifulSoup
from httprunner import __version__
from libs.model_001 import *
from libs.model_002 import *

def get_execution(host):
    # 从get登录的html中获取post登录的变量值，传递给登录
    res = requests.get(url=f"https://{host}:8888/cas/login", verify=False)
    execution = BeautifulSoup(res.text, "lxml").find(attrs={"name":"execution"})["value"]
    return execution

def get_httprunner_version():
    return __version__


if __name__ == '__main__':
    get_execution()

