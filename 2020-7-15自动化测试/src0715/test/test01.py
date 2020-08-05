#
#功能：实现unittest框架中的 构建测试套件，批量执行脚本
#


import unittest
from src0715 import test_080302
from src0715 import test_080301

def createsuite():

    #注释多行快捷键：选中+Ctrl+/，取消多行注释，再次按下Ctrl+/
    #测试套件
    #以下每一个方法的应用场景都不同，所以不存在哪一个方法好，哪一个不好
    #。self在定义类的方法时是必须有的，然后为了方便在类的方法中引用当前对象，就引入了一些关键字（python里是self，Java里是this）。

    # #方法——01——使用addTest方法
    # suite = unittest.TestSuite()
    # #将测试用例加载到测试容器（套件）中
    # suite.addTest(test_080301.Test080301("test_1"))
    # suite.addTest(test_080302.Test080302("test_2"))
    # suite.addTest(test_080302.Test080302("test_3"))
    # return suite

    # #方法——02——使用makeSuite方法
    # suite = unittest.TestSuite()
    # #将测试用例加载到测试容器（套件）中
    # suite.addTest(unittest.makeSuite(test_080301.Test080301))
    # suite.addTest(unittest.makeSuite(test_080302.Test080302))
    # return suite

    # #方法——03——使用TestLoader方法
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(test_080301.Test080301)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(test_080302.Test080302)
    # suite = unittest.TestSuite([suite1, suite2])
    # return suite

    #方法——04——使用discover方法——当需要执行的方法比较多时，在一个文件夹下，将所有的相同类型的文件都加载出来，效率高
    # discovers = unittest.defaultTestLoader.discover("../src0715", pattern="test*.py", top_level_dir=None)
    discovers = unittest.defaultTestLoader.discover("src0715", pattern="test*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__ == "__main__":
    suite = createsuite()
    # runner = unittest.TextTestRunner(verbosity=0)  # 用0的话，这里输出的结果是：总的成功和失败的测试用例数
    # runner = unittest.TextTestRunner(verbosity=1)# 用1的话，这里输出的结果是比较简略的，每一个成功前面是“."，每一个失败后是”F“
    runner = unittest.TextTestRunner(verbosity=2)  # 用2的话，这里输出的结果是比较详细的
    runner.run(suite)
