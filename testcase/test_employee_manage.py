import allure
import pytest
import os
import yaml

from api.Employee_Manage import EmployeeManage
from utils.MyLog import MyLog
from utils.Return_data import My_return_data
from utils.commen_assert import common_assert


@allure.step('员工增删改查流程测试-从manage_employee获取数据')
def build_data():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'driver_data', 'manage_employee.yaml')
    with open(file_path, mode= 'r', encoding= 'utf-8') as f:
        doc = yaml.load(f, Loader= yaml.FullLoader)
    return doc


@allure.epic('基本信息管理模块')
@allure.feature('新增员工测试')
class Test_add_employee():

    @allure.story('员工新增数据驱动测试')
    @allure.title('{title}')
    @pytest.mark.usefixtures('re_login')
    @pytest.mark.parametrize('title, add_data, expected', My_return_data.return_test_data('add_employee.yaml'))
    def test_add_empolyee(self, environment_url, add_data, expected, title, get_token):
        try:
            res = EmployeeManage().add_employee(environment_url, add_data, get_token)
            common_assert(res, expected)
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

@allure.epic('基本信息管理模块')
@allure.feature('修改员工测试')
class Test_modify_employee():

    employee_id = '1439429426361139200'
    @allure.story('修改员工(1439429426361139200)，数据驱动测试')
    @allure.title('{title}')
    @pytest.mark.usefixtures('re_login')
    @pytest.mark.parametrize('title, modify_data, expected', My_return_data.return_test_data('modify_employee.yaml'))
    def test_modify_employee(self, environment_url, modify_data, expected, title, get_token):
        try:
            res = EmployeeManage().modify_employee(environment_url, Test_modify_employee.employee_id, modify_data, get_token)
            common_assert(res, expected)
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

@allure.epic('基本信息管理模块')
@allure.feature('查询员工(1439429426361139200)测试')
class Test_query_employee():

    employee_id = '1439429426361139200'
    @allure.story('查询员工单接口测试')
    @allure.title('查询员工id：1439429426361139200')
    @pytest.mark.usefixtures('re_login')
    def test_modify_employee(self, environment_url, get_token):
        try:
            res = EmployeeManage().query_employee(environment_url, Test_modify_employee.employee_id, get_token)
            with allure.step('断言username修改为jack1666t5555512'):
                assert 200 == res.status_code
                assert 'jack1666t5555512' == res.json().get('data').get('username')
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

@allure.epic('基本信息管理模块')
@allure.feature('员工管理流程测试')
class Test_employee_manage():

    employee_id = None
    @allure.story('员工增删改查流程测试')
    @allure.title('员工增删改查，但删除会失败验证')
    @pytest.mark.usefixtures('re_login')
    def test_employee_manage(self, environment_url, get_token):
        try:
            data = build_data()
            res = EmployeeManage().add_employee(environment_url, data.get('add_data'), get_token)
            common_assert(res, data.get('expected'))
            with allure.step('获取新增员工ID'):
                Test_employee_manage.employee_id = res.json().get('data').get('id')
            with allure.step('验证查询员工username与新增员工一致'):
                res = EmployeeManage().query_employee(environment_url, Test_employee_manage.employee_id, get_token)
                assert data.get('add_data').get('username') == res.json().get('data').get('username')
            res = EmployeeManage().modify_employee(environment_url, Test_employee_manage.employee_id, data.get('modify_data'), get_token)
            common_assert(res, data.get('expected'))
            with allure.step('验证查询员工username与修改后员工一致'):
                res = EmployeeManage().query_employee(environment_url, Test_employee_manage.employee_id, get_token)
                assert data.get('modify_data').get('username') == res.json().get('data').get('username')
            res = EmployeeManage().delete_employee(environment_url, Test_employee_manage.employee_id, get_token)
            common_assert(res, data.get('expected'))
            with allure.step('验证删除员工后，查询员工返回空'):
                res = EmployeeManage().query_employee(environment_url, Test_employee_manage.employee_id, get_token)
                common_assert(res, data.get('expected_after_delete'))
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e



if __name__ == '__main__':
    # pytest.main(['-s', '-v', 'test_employee_manage.py', '--alluredir=../report/result'])
    pytest.main(['-s', '-v', '--alluredir=../report/result'])
    os.system('allure generate ../report/result -o ../report/html --clean')