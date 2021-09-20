import requests
import allure

class Login_Api():


    @allure.step('登陆操作')
    def login(self, url, login_data):
        url = url + '/api/sys/login'
        res = requests.post(url= url, json= login_data)
        return res