

from controller import login
import unittest

class Testlogin(unittest.TestSuite):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('开始执行用例')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('结束测试用例')
    #
    #
    # def setUp(self) -> None:
    #     print('初始化')
    #
    # def tearDown(self) -> None:
    #     print('清空')

    def test_login1(self):
        print('test1')
        self.assertEqual("登录成功",login('admin','123456'))

    def test_login2(self):
        self.assertEqual("用户名为空",login('','123456'))

    def test_login3(self):
        self.assertEqual("密码为空",login('admin',''))

    def test_login4(self):
        self.assertEqual("密码错误",login('','123456'))



# import requests
# import unittest
#
# class logintest(unittest.TestCase):   #测试类名
#     def setUp(self):                      #用固件setUp初始化
#         self.url = "http://192.168.1.224:8086/smt/login/userLogin.as"
#     def testlogin1(self):
#         form = {"username":"smtadmin","password":123456}
#         r = requests.post(self.url,data=form)
#         self.assertEqual(r.text,"登录成功")                  #断言验证
#     def testlogin2(self):
#         form = {"username":"","password":123456}
#         r = requests.post(self.url,data=form)
#         self.assertEqual(r.test,"用户名不能为空")
#
#     def testlogin3(self):
#         form = {"username":"smtadmin","password":""}
#         r= requests.post(self.url,date=form)
#         self.assertEqual(r.text,"密码不能为空")
#     def testlogin4(self):
#         form = {"username":"smtadmin","password":"111111"}
#         r = requests.post(self.url,data=form)
#         self.assertEqual(r.text,"账户或密码错误")

suite = unittest.TestSuite()
# suite.addTest(logintest('testlogin2'))
# suite.addTest(logintest('testlogin3'))
# suite.addTest(logintest('testlogin4'))

# caselist=[logintest('testlogin2'),logintest('testlogin3'),logintest('testlogin4')]
# suite.addTests(caselist)
#
#
# runner = unittest.TextTestRunner()
# runner.run(suite)