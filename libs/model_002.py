import time
import os


# 获取最新时间戳
def get_timestamp():
    return int(time.time() * 1000)

def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_encrypt_password():
    raw_passwd = os.environ["Password"]
    PROJECT_KEY = os.environ["PROJECT_KEY"]
    password = (raw_passwd + PROJECT_KEY).encode('ascii')
    return 2

def get_account(num):
    accounts = []
    for index in range(1, num+1):
        accounts.append({"username": "user%s" % index, "password": str(index) * 6},)
    return accounts