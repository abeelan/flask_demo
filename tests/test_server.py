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
        assert r.status_code == 200

    def test_post(self):
        r = requests.post(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_put(self):
        r = requests.put(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_delete(self):
        r = requests.delete(self.base_url)
        print(r.json())
        assert r.status_code == 200
