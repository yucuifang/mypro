import json
import unittest
import common.Log

import paramunittest

from common.configHttp import RunMain
import geturlParams
import readjson

log = common.Log.logger
testData = readjson.readJson().read_json("links/link_name_unique_script.json")

# @paramunittest.parametrized("test")
class testIsUniqueLinkName(unittest.TestCase):
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
        log.info("testIsUniqueLinkName 测试开始前准备")

    def test_is_unique_link_name(self):
        self.setUp()
        self.checkResult()
        self.tearDown()

    def tearDown(self):
        log.info("testIsUniqueLinkName 测试结束，输出log完结")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        for data in testData:
            url = geturlParams.geturlParams().get_Url("/is-link-name-unique?name="+data['name'])  # 调用我们的geturlParams获取我们拼接的URL
            info = RunMain().run_main("get", url)  # 调用run_main来进行requests请求，并拿到响应
            ret = json.loads(info)  # 将响应转换为字典格式
            test_ret = False
            if ret['code'] != data['ret_code'] and "data" in ret and ret['data'] == data['data']:
                test_ret = True
            log_info = "test description:{des},\ntest param:{param},\ntest result:{test_ret},\nresult_info:{ret_info}". \
                format(des=data['testDescription'], param=data, test_ret=test_ret, ret_info=ret)
            log.info(log_info)
            print('param', data)
            print('result', ret)
            # self.assertEqual(test_ret, True)



if __name__ == "__main__":
    testIsUniqueLinkName().test_is_unique_link_name()
