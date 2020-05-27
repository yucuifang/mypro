import json
import getpathInfo
import os

# 拿到该项目所在的绝对路径
path = getpathInfo.get_Path()

class readJson():
    def read_json(self, file_name):
        file_path = os.path.join(path, "testFile", 'case', file_name)
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取json文件的值
    print(readJson().read_json('create_term_template_script.json'))