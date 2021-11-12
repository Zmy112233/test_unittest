import unittest
from HTMLTestRunner import HTMLTestRunner

# 1、创建套件
suite = unittest.TestLoader().discover(r'D:\ceshi\pythondemo\test_unittest',pattern='test*.py')


# 2、生成文件
report_path = 'test_report.html'

with open(report_path,'wb') as f:

# # 创建运行器
# runner = unittest.TextTestRunner()
# runner.run(suite)
    runner = HTMLTestRunner(f,title='测试报告1',description='v1.1')
    runner.run(suite)