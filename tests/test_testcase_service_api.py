"""
@Time   : 2021/9/30 下午1:27
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 单元测试用例
"""
import random
import requests


class TestTestcaseService():

    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/testcase"

    def test_get(self):
        r = requests.get(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_get_by_id(self):
        data = requests.get(self.base_url).json()
        id = data["data"][0]["id"]

        r = requests.get(self.base_url, params={"id": id})
        print(r.json())
        assert r.status_code == 200

    def test_get_by_id_not_match(self):
        r = requests.get(self.base_url, params={"id": 0})
        assert r.status_code == 200
        assert r.json()["error"] == 40004

    def test_post(self):
        # 添加用例数据
        # data = {"id": 1, "nodeId": "node01", "remark": "remark01"}
        data = {"id": 2, "nodeId": "node02", "remark": "remark02"}
        r = requests.post(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200

    def test_post_nodeId_list(self):
        """测试 node id 为列表时"""
        id = random.randint(1, 1000),
        id = id[0]

        data = {
            "id": id,
            "nodeId": str(id),
            "remark": "我是备注"
        }
        r = requests.post(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        data = {"id": 1, "nodeId": "node02-modify", "remark": "remark02-modify"}
        r = requests.put(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200

    def test_delete_fail(self):
        r = requests.delete(self.base_url)
        print(r.json())
        assert r.json()["error"] == 40001
        assert r.status_code == 200

    def test_delete_success(self):
        r = requests.delete(self.base_url, params={"id": 2})
        print(r.json())
        assert r.json()["error"] == 0
