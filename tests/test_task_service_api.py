"""
@Time   : 2021/10/13 下午11:57
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
import requests

from apis.task import TaskService


class TestTaskService:

    def setup_class(self):
        self.url = "http://127.0.0.1:5000/task"

    def test_get(self):
        r = requests.get(self.url)
        assert r.status_code == 200

    def test_post(self):
        data = {"nodeId": "test_demo.py"}
        r = requests.post(self.url, json=data)
        assert r.status_code == 200


