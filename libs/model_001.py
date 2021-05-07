import uuid
import os, time


def get_chengdu20_mapname():
    """获取某个目录下的所有文件的文件名，不包括后缀名。该测试路径下下只有文件，没有目录。
    :return:
    """
    file = "//ip//目录//目录"
    li = [n.split(".")[0] for i in os.walk(file) for n in i[2]]
    print(li)
    return li

# 随机生成一串字符串
def gen_nodeid():
    return str(uuid.uuid4())

