"""
@Time   : 2021/9/30 下午1:27
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
import requests


class TestServer():

    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/server"

    def test_get(self):
        r = requests.get(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_get_by_id(self):
        r = requests.get(self.base_url, params={"id": 2})
        print(r.json())
        assert r.status_code == 200

    def test_post(self):
        # 添加用例数据
        # data = {"id": 1, "node_id": "node01", "remark": "remark01"}
        data = {"id": 2, "node_id": "node02", "remark": "remark02"}
        r = requests.post(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200

    def test_post_node_id_list(self):
        """测试 node id 为列表时"""
        data = {"id": 34, "node_id": ["node3", "node4"], "remark": "remark0304"}
        r = requests.post(self.base_url, json=data)
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        data = {"id": 2, "node_id": "node02-modify", "remark": "remark02-modify"}
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
