import allure
import requests

class EmployeeManage():
    '''
    员工管理类
    '''
    @allure.step('发送新增员工请求，获取响应体')
    def add_employee(self, url, add_data, token):
        '''
        新增员工接口，前置条件：登陆
        :param url:环境IP地址
        :param add_data: {'username': , 'mobile':  等}
        :param token: {'Authorization': 'Bearer f5050a1b-7919-444c-9ec4-
3c1a7286536d
'}用户令牌
        :return: 新增员工响应体
        '''
        url = url + '/api/sys/user'
        res = requests.post(url= url, json= add_data, headers= token)
        return res

    @allure.step('发送查询员工请求，获取响应体')
    def query_employee(self, url, employee_id, token):
        '''
        查询员工接口，前置条件：登陆
        :param url: 环境IP地址
        :param employee_id: 员工id,员工唯一标识，新增员工时返回，152X1523S522
        :param token: 用户令牌
        :return: 查询员工响应体
        '''
        url = url + '/api/sys/user/{}'.format(employee_id)
        res = requests.get(url= url, headers= token)
        return res

    @allure.step('发送修改员工请求，获取响应体')
    def modify_employee(self, url, employee_id, modify_data, token):
        '''
        修改员工接口，前置条件：登陆
        :param url: 环境IP地址
        :param employee_id: 员工id,员工唯一标识，新增员工时返回，152X1523S522
        :param modify_data: {'username': , 'mobile':  等}
        :param token: 用户令牌
        :return: 修改员工响应体
        '''
        url = url + '/api/sys/user/{}'.format(employee_id)
        res = requests.put(url= url, json= modify_data, headers= token)
        return res

    @allure.step('发送删除员工请求，获取响应体')
    def delete_employee(self, url, employee_id, token):
        '''
        删除员工接口，前置条件：登陆
        :param url: 环境IP地址
        :param employee_id: 员工id,员工唯一标识，新增员工时返回，152X1523S522
        :param token: 用户令牌
        :return: 删除员工响应体
        '''
        url = url + '/api/sys/user/{}'.format(employee_id)
        res = requests.delete(url= url, headers= token)
        return res