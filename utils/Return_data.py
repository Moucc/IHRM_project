import os
import yaml

from utils.MyLog import MyLog


def check_file_name(file_name):
    path = file_name[0: file_name.rfind('\\')]
    if not os.path.isdir(path):
        e = str(path) + '路径不存在'
        MyLog.error(e)
        raise FileNotFoundError
    if not os.path.isfile(file_name):
        e = str(file_name) + '数据文件不存在'
        MyLog.error(e)
        raise FileNotFoundError

class My_return_data():

    @staticmethod
    def return_test_data(file_name):
        '''
        解析ymal文件中的(ask, excepted)作为数据驱动
        :param file_name: 文件名，前置路径为D:\IHRM_project\data\driver_data
        :return: 返回字典数据[(ask, excepted), ]，多组数据组成的字典，可做数据驱动
        '''
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\data\\driver_data\\' + str(file_name)
        check_file_name(path)
        test_data = []
        with open(path, mode='r', encoding= 'utf-8') as f:
            doc = yaml.load(f, Loader= yaml.FullLoader)
            for data in doc:
                title = data.get('test').get('title')
                ask = data.get('test').get('ask')
                excepted = data.get('test').get('excepted')
                test_data.append((title, ask, excepted))
        return test_data


if __name__ == "__main__":
    print(My_return_data.return_test_data('login_d1ata.yaml'))
