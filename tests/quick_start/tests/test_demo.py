"""
@Time   : 2021/9/30 上午2:03
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   :
"""
import requests


class TestDemo:

    def test_request_json(self):
        data = {
            "a": 1,
            "b": 2
        }
        r = requests.post("http://127.0.0.1:5000/request_json", json=data)
        assert r.json()["a"] == 1
        assert r.json()["b"] == 2



