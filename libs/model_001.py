import uuid

# 这里是根目录的标记
from httprunner import __version__


def get_httprunner_version():
    return __version__

def gen_memeberid():
    return "5242742441223623"

# 随机生成一串字符串
def gen_nodeid():
    return str(uuid.uuid4())
