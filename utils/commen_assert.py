from utils.MyLog import MyLog
import allure

@allure.step('进行断言')
def common_assert(res, expected):
    '''
    对响应体进行断言
    :param res: 请求响应体
    :param expected: 字典：{success: true， code: 10000， message: '操作成功'， status_code: 200}
    :return:assert断言
    '''
    assert expected.get('status_code') == res.status_code
    assert expected.get('code') == res.json().get('code')
    assert expected.get('message') in res.json().get('message')
    assert expected.get('success') == res.json().get('success')