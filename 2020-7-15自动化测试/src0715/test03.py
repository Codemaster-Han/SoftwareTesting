#
#功能：实现HTML测试报告生成
#

import unittest
import os
import sys
import time
import re
import HTMLTestRunner
#from src0715 import test_080302

def createsuite():
    discovers = unittest.defaultTestLoader.discover("src0715", pattern="test*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__ == "__main__":
    curpath = sys.path[0]
    print(sys.path)
    print("===========")
    print(sys.path[0])
    # 创建存放测试报告的文件夹
    if not os.path.exists(curpath+'/resultreportFile'):
        os.makedirs(curpath+'/resultreportFile')
    # 取当前时间，用当前时间对测试报告的文件进行命名，则不会出现每次运行文件会被覆盖的情况
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))#strftime是格式化，time.localtime是本地时间，time.time()是时间戳
    print(time.localtime(time.time()))
    print("=======================")
    print(now)
    # 经过上述步骤，已经得到了HTML报告的名称
    filename = curpath+'/resultreportFile/'+now+ 'resultreport.html'
    # 打开HTML文件，wb 以写的方式，输入流fp
    # 输出html报告
    # 括号里面的参数是HTML报告里面的参数
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况", verbosity=2)# 用2的话，这里输出的结果是比较详细的
        suite = createsuite()
        runner.run(suite)

