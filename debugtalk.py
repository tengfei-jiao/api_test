from libs.model_001 import *
from libs.model_002 import *


# 配置环境的sesion,token
huanjing = [1, 2, 3]
def gen_session():
    if huanjing == 1:
        return "token1"
    elif huanjing ==2:
        return "token2"
    elif huanjing == 3:
        return "token3"

