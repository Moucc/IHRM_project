import logging
import os
import traceback



logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

#只能在方法中调用类的属性，无法直接在最外层文件直接调用，外层直接调用未编译找不到？MyLog.handler直接在外层调用是无法找到的
def set_handler():
    logger.addHandler(MyLog.handler)

def remove_handler():
    logger.removeHandler(MyLog.handler)

class MyLog():
    #判断文件路径、文件是否存在
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = path + '\log\log.log'
    dir_path = file_path[0: file_path.rfind('\\')]
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    if not os.path.isfile(file_path):
        fd = open(file_path, mode= 'w', encoding= 'utf-8')
        fd.close()
    else:
        pass


    #handler  fomatter 都是logging创建
    #创建handler，为handler  setformatter
    handler = logging.FileHandler(file_path, encoding='utf-8')
    file_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(file_formatter)


    #在类的方法中也无法调用未用self定义的属性，只能通过外层定义函数调用再传入
    @staticmethod
    def error(mesg):
        set_handler()
        logger.error(str(mesg) + '\n' + traceback.format_exc())
        remove_handler()

    @staticmethod
    def debug(mesg):
        set_handler()
        logger.debug(str(mesg) + '\n' + traceback.format_exc())
        remove_handler()

    @staticmethod
    def warning(mesg):
        set_handler()
        logger.warning(str(mesg) + '\n' + traceback.format_exc())
        remove_handler()

    @staticmethod
    def info(mesg):
        set_handler()
        logger.info(str(mesg) + '\n' + traceback.format_exc())
        remove_handler()

    @staticmethod
    def critical(mesg):
        set_handler()
        logger.critical(str(mesg) + '\n' + traceback.format_exc())
        remove_handler()

if __name__ == '__main__':
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(os.path.abspath(__file__)[0: os.path.abspath(__file__).rfind('\\') -6])
    MyLog.error('error')
    MyLog.critical('critical')
    MyLog.info('info')
    MyLog.warning('warning')
    MyLog.debug('debug')
