#
# 使用unittest测试框架中的TestCase类,TestSuite方法,，构建测试套件，批量执行脚本
# 使用断言方法
# 功能：实现HTML测试报告生成
# 功能：实现 异常捕捉和错误截图
#

import unittest
import os
import sys
import time
import re
import HTMLTestRunner
from src0812 import test0813

def createsuite():

    #注释多行快捷键：选中+Ctrl+/，取消多行注释，再次按下Ctrl+/
    #测试套件
    #以下每一个方法的应用场景都不同，所以不存在哪一个方法好，哪一个不好
    #。self在定义类的方法时是必须有的，然后为了方便在类的方法中引用当前对象，就引入了一些关键字（python里是self，Java里是this）。

    # #方法——01——使用addTest方法
    # suite = unittest.TestSuite()
    # #将测试用例加载到测试容器（套件）中
    # suite.addTest(test0813.TestChrom01("test_01"))
    # suite.addTest(test0813.TestChrom01("test_02"))
    # suite.addTest(test0813.TestChrom01("test_03"))
    # suite.addTest(test0813.TestChrom01("test_04"))
    # return suite

    # #方法——02——使用makeSuite方法--最合适
    # suite = unittest.TestSuite()
    # #将测试用例加载到测试容器（套件）中
    # suite.addTest(unittest.makeSuite(test0813.TestChrom01))
    # return suite

    # #方法——03——使用TestLoader方法
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(test0813.TestChrom01)
    # suite = unittest.TestSuite(suite1)
    # return suite

    #方法——04——使用discover方法——当需要执行的方法比较多时，在一个文件夹下，将所有的相同类型的文件都加载出来，效率高
    discovers = unittest.defaultTestLoader.discover("../src0812", pattern="test08*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__ == "__main__":
    curpath = sys.path[0]
    print(sys.path[0])
    # 创建存放测试报告的文件夹
    if not os.path.exists(curpath+'/resultreportFile'):
        os.makedirs(curpath+'/resultreportFile')
    # 取当前时间，用当前时间对测试报告的文件进行命名，则不会出现每次运行文件会被覆盖的情况
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))#strftime是格式化，time.localtime是本地时间，time.time()是时间戳
    # 经过上述步骤，已经得到了HTML报告的名称
    filename = curpath+'/resultreportFile/'+now+ 'resultreport.html'
    # 打开HTML文件，wb 以写的方式，输入流fp
    # 输出html报告
    # 括号里面的参数是HTML报告里面的参数
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况", verbosity=2)# 用2的话，这里输出的结果是比较详细的
        suite = createsuite()
        # runner = unittest.TextTestRunner(verbosity=0)  # 用0的话，这里输出的结果是：总的成功和失败的测试用例数
        # runner = unittest.TextTestRunner(verbosity=1)# 用1的话，这里输出的结果是比较简略的，每一个成功前面是“."，每一个失败后是”F“
        # runner = unittest.TextTestRunner(verbosity=2)  # 用2的话，这里输出的结果是比较详细的
        runner.run(suite)