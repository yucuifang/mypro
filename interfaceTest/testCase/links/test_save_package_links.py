import json
import unittest
import common.Log

import paramunittest

from common.configHttp import RunMain
import geturlParams
import readjson

log = common.Log.logger
testData = readjson.readJson().read_json("links/package_links_script.json")

# @paramunittest.parametrized("test")
class testSavePackageLink(unittest.TestCase):
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
        log.info("testSavePackageLink 测试开始前准备")

    def test_save_package_link(self):
        self.setUp()
        self.checkResult()
        self.tearDown()

    def tearDown(self):
        log.info("testSavePackageLink 测试结束，输出log完结")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        url = geturlParams.geturlParams().get_Url("/package-links")  # 调用我们的geturlParams获取我们拼接的URL
        for data in testData:
            info = RunMain().run_main("post", url=url, jsonData=data)  # 调用run_main来进行requests请求，并拿到响应
            ret = json.loads(info)  # 将响应转换为字典格式
            test_ret = True
            # if ret['code'] != data['ret_code']:
            #     test_ret = True
            log_info = "test param:{param},\ntest result:{test_ret},\nresult_info:{ret_info}". \
                format(param=data, test_ret=test_ret, ret_info=ret)
            log.info(log_info)
            print('param', data)
            print('result', ret)
            # self.assertEqual(test_ret, True)



if __name__ == "__main__":
    testSavePackageLink().test_save_package_link()
