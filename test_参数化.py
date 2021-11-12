import unittest
from parameterized import parameterized
from controller import login


class Testlogin(unittest.TestCase):

    @parameterized.expand([("登录成功",'admin','123456'),("密码为空",'admin',''),("用户名为空",'','123456')])
    def test_login(self,expect,username,password):
        self.assertEqual(expect,login(username,password))
