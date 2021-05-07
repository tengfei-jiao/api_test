# NOTE: Generated By HttpRunner v3.1.4
# FROM: har\mubu_creat_doc.har
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

# 改名是为了防止用例执行时候执行了TestCaseMubuLogin
from testcases.mubu_login_test import TestCaseMubuLogin as MubuLogin

import pytest
from httprunner import Parameters


class TestCaseMubuCreatDoc(HttpRunner):
    @pytest.mark.parametrize("param", Parameters({"mapname": "${get_chengdu20_mapname()}"}))
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("login mubu")
        .variables(phone="${ENV(username)}", password="${ENV(password)}", host="${ENV(host)}")
        .verify(False)
        .base_url("https://${host}")
        .export(*["unreadCount"])
    )

    teststeps = [
        Step(
            RunTestCase("这里调用登录的用例，传递出三个会话的变量。")
            .call(MubuLogin)
            .export(*["tgc_login",
                      "genex_session",
                      "jessionid_fusiongissaccess"])
        ),
        Step(
            RunRequest("这里是上传文件的接口")
            .post("https://{host}:8888/xxx/upload.do")
            .with_headers("xxx")
            .with_cookies("xxx")
            .upload(file = "//ip//目录//目录//$mapname.zip",
                    mapname = "",
                    usage = "xx",
                    description = "")
            .validate()
            .assert_equal("status_code", 200)
        )]


if __name__ == "__main__":
    TestCaseMubuCreatDoc().test_start()