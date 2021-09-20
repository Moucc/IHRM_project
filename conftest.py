import pytest
import os
import yaml
import allure
import json

from api.Login import Login_Api
from utils.MyLog import MyLog


@allure.title('从config.yaml获取环境IP')
@pytest.fixture()
def environment_url(request):
    try:
        path = os.path.join(request.config.rootdir, 'config', 'config.yaml')
        with open(path, 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
            return doc.get('host')
    except Exception as e:
        MyLog.error(e)
        raise e

@allure.title('前置登陆操作')
@pytest.fixture()
def re_login(environment_url):
    try:
        login_data = {'mobile': '13800000002',
          'password': '123456'}
        res = Login_Api().login(environment_url, login_data)
        token = {'Authorization': 'Bearer ' + res.json().get('data')}
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'transfer_data', 'login_token.json')
        with open(file_path, mode= 'w', encoding= 'utf-8') as f:
            json.dump({'token': token}, f)
            f.close()
    except Exception as e:
        MyLog.error(e)
        raise e

@allure.title('获取token')
@pytest.fixture()
def get_token():
    try:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'transfer_data', 'login_token.json')
        with open(file_path, 'r') as f:
            doc = json.load(f)
            token = doc.get('token')
        return token
    except Exception as e:
        MyLog.error(e)
        raise e


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")