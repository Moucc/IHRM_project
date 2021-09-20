import requests
import allure

class Department_Manage():

    @allure.step('查询所有部门信息')
    def query_all_department(self, url, token):
        '''
        查询所有部门信息，需前置登陆操作，获取token令牌
        :param url: 环境IP
        :param token: 用户令牌{Authorization: Bearer 444}
        :return: 查询响应体{"success": true,
                            "code": 10000,
                            "message": "操作成功！",
                            "data": {
                                "companyId": "1",
                                "companyName": "江苏传智播客教育科技股份有限公司",
                                "companyManage": "张三",}
                            depts{            {
                                "id": "1436297561253183488",
                                "pid": null,
                                "companyId": "1",
                                "name": "来测试啊",
                                "code": "333",
                                "managerId": null,
                                "manager": null,
                                "introduce": null,
                                "createTime": null
                            },
                            }
        '''
        url = url + '/api/company/department'
        res = requests.get(url, headers= token)
        return res

    @allure.step('查询指定部门信息')
    def query_a_department(self, url, token, id):
        '''
        查询指定部门信息，需前置登陆操作，获取token令牌
        :param url: 环境IP
        :param token: 用户令牌{Authorization: Bearer 444}
        :param id: 部门ID
        :return: 查询响应体{
                        "success": true,
                        "code": 10000,
                        "message": "操作成功！",
                        "data": {
                            "id": "1439852389577359360",
                            "pid": "9527",
                            "companyId": "1",
                            "name": null,
                            "code": null,
                            "managerId": null,
                            "manager": "部门负责人",
                            "introduce": "部门描述",
                            "createTime": null}
                        }
        '''
        url = url + '/api/company/department/{}'.format(id)
        res = requests.get(url, headers= token)
        return res

    @allure.step('添加部门')
    def add_department(self, url, token, add_data):
        '''
        添加部门，需前置登陆操作，获取token令牌
        :param url: 环境IP
        :param token: 用户令牌{Authorization: Bearer 444}
        :param add_data: {name: , code: , manager: , introduce: , pid: }
        :return:{
                "success": true,
                "code": 10000,
                "message": "操作成功！",
                "data": {
                    "id": "1439852389577359360"
                }
            }
        '''
        url = url + '/api/company/department'
        res = requests.post(url, json= add_data, headers= token)
        return res

    @allure.step('修改部门信息')
    def modify_department(self, url, token, modify_data, id):
        '''
        修改部门，需前置登陆操作，获取token令牌
        :param url: 环境IP
        :param token: 用户令牌{Authorization: Bearer 444}
        :param modify_data: {name: , code: , manager: , introduce:  }
        :param id: 部门ID
        :return:{
                "success": true,
                "code": 10000,
                "message": "操作成功！",
                "data": null
            }
        '''
        url = url + '/api/company/department/{}'.format(id)
        res = requests.put(url, json= modify_data, headers= token)
        return res

    @allure.step('删除部门信息')
    def delete_department(self, url, token, id):
        '''
        删除部门，需前置登陆操作，获取token令牌
        :param url: 环境IP
        :param token: 用户令牌{Authorization: Bearer 444}
        :param id: 部门ID
        :return:{
                "success": true,
                "code": 10000,
                "message": "操作成功！",
                "data": null
            }
        '''
        url = url + '/api/company/department/{}'.format(id)
        res = requests.delete(url, headers= token)
        return res