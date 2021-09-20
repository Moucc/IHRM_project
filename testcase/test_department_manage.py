import pytest
import allure
import os

import yaml

from api.Department_Manage import Department_Manage
from utils.MyLog import MyLog
from utils.Return_data import My_return_data
from utils.commen_assert import common_assert

@allure.step('部门管理-增删改查正向流程测试，从manage_department.yaml获取数据')
def build_data():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'driver_data', 'manage_department.yaml')
    with open(file_path, mode= 'r', encoding= 'utf-8') as f:
        doc = yaml.load(f, Loader= yaml.FullLoader)
    return doc

@allure.epic('基本信息管理模块')
@allure.feature('部门管理模块')
class Test_department_manage():

    null_id = []
    @allure.story('查询部门所有信息单接口测试')
    @allure.title('查询部门所有信息单接口测试')
    @pytest.mark.usefixtures('re_login')
    def test1_query_all_department(self, environment_url, get_token):
        try:
            res = Department_Manage().query_all_department(environment_url, get_token)
            with allure.step('断言响应中depts is not null'):
                assert 200 == res.status_code
                assert True == res.json().get('success')
                assert 10000 == res.json().get("code")
                assert '操作成功' in res.json().get('message')
                assert len(res.json().get('data').get('depts')) > 0
            with allure.step('整理所有createTime为null的部门信息,为删除做准备'):
                for data in res.json().get('data').get('depts'):
                    if not data.get('createTime'):
                        Test_department_manage.null_id.append(data.get('id'))
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

    @allure.story('删除部门信息')
    @allure.title('删除所有createTime为null的部门信息')
    @pytest.mark.usefixtures('re_login')
    def test_delete_department(self, environment_url, get_token):
        try:
            for id in Test_department_manage.null_id:
                res = Department_Manage().delete_department(environment_url, get_token, id)
                with allure.step('断言响应操作成功'):
                    assert 200 == res.status_code
                    assert True == res.json().get('success')
                    assert 10000 == res.json().get("code")
                    assert '操作成功' in res.json().get('message')
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

    @allure.story('新增部门信息-数据驱动测试')
    @allure.title('{title}')
    @pytest.mark.usefixtures('re_login')
    @pytest.mark.parametrize('title, ask, excepted', My_return_data.return_test_data('add_department.yaml'))
    def test_add_department(self, environment_url, get_token, title, ask, excepted):
        try:
            res = Department_Manage().add_department(environment_url, get_token, ask)
            common_assert(res, excepted)
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

    @allure.story('部门管理流程测试')
    @allure.title('部门管理-增删改查正向流程测试')
    @pytest.mark.usefixtures('re_login')
    def test_manage_department(self, environment_url, get_token):
        try:
            data = build_data()
            res = Department_Manage().add_department(environment_url, get_token, data.get('add_data'))
            common_assert(res, data.get('expected'))
            with allure.step('获取新增部门ID，为修改、查询、删除部门信息做准备'):
                id = res.json().get('data').get('id')
            res = Department_Manage().modify_department(environment_url, get_token, data.get('modify_data'), id)
            common_assert(res, data.get('expected'))
            with allure.step('查询验证修改的信息introduce正确'):
                res = Department_Manage().query_a_department(environment_url, get_token, id)
                assert data.get('modify_data').get('introduce') == res.json().get('data').get('introduce')
            res = Department_Manage().delete_department(environment_url, get_token, id)
            common_assert(res, data.get('expected'))
            with allure.step('查询验证部门信息已被删除'):
                res = Department_Manage().query_a_department(environment_url, get_token, id)
                common_assert(res, data.get('expected_delete'))
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e


if __name__ == '__main__':
    # pytest.main(['-s', 'test_department_manage.py', '--alluredir=../report/result'])
    pytest.main(['-s', '--alluredir=../report/result'])
    os.system('allure generate ../report/result -o ../report/html --clean')