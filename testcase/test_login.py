import pytest
import allure
import os


from api.Login import Login_Api
from utils.Return_data import My_return_data
from utils.commen_assert import common_assert
from utils.MyLog import MyLog

@allure.epic('登陆')
@allure.feature('多场景登陆测试')
class Test_login():

    @allure.story('数据驱动登陆测试')
    @allure.title('{title}')
    @pytest.mark.parametrize('title, ask, expected', My_return_data.return_test_data('login_data.yaml'))
    def test_login(self, environment_url, ask, expected, title):
        try:
            res = Login_Api().login(environment_url, ask)
            common_assert(res, expected)
        except Exception as e:
            err = str(res.json()) + '\n' + str(e)
            MyLog.error(err)
            raise e

if __name__ == '__main__':
    # pytest.main(['-s', '-v', 'test_login.py'])
    pytest.main(['-s', '-v', '--alluredir=../report/result'])
    os.system('allure generate ../report/result -o ../report/html --clean')