import json
import unittest
import common.Log

import paramunittest

from common.configHttp import RunMain
import geturlParams
import readjson

log = common.Log.logger
testData = readjson.readJson().read_json("links/disable_links_script.json")

# @paramunittest.parametrized("test")
class testDisableLink(unittest.TestCase):
    def setParameters(self, case_name):
        """
        set params
        :param case_name:
        :return:
        """
        # self.case_name = str(case_name)
        # self.path = str(path)
        # self.query = str(query)
        # self.method = str(method)

    def setUp(self):
        """
        :return:
        """
        log.info("testDisableLink 测试开始前准备")

    def test_disable_link(self):
        self.setUp()
        self.checkResult()
        self.tearDown()

    def tearDown(self):
        log.info("testDisableLink 测试结束，输出log完结")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        url = geturlParams.geturlParams().get_Url("/disable-link")  # 调用我们的geturlParams获取我们拼接的URL
        for data in testData:
            info = RunMain().run_main("post", url, data)  # 调用run_main来进行requests请求，并拿到响应
            ret = json.loads(info)  # 将响应转换为字典格式
            test_ret = False
            if ret['code'] != data['ret_code']:
                test_ret = True
            log_info = "test description:{des},\ntest param:{param},\ntest result:{test_ret},\nresult_info:{ret_info}". \
                format(des=data['testDescription'], param=data, test_ret=test_ret, ret_info=ret)
            log.info(log_info)
            print('param', data)
            print('result', ret)
            # self.assertEqual(test_ret, True)



if __name__ == "__main__":
    testDisableLink().test_disable_link()
