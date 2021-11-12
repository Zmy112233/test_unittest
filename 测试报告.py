
import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('.', pattern="test*.py")

flame = '测试报告.html'
# f = open(flame,'wb')
# runner = HTMLTestRunner(f,title='报告',description='v1.0')
# runner.run(suite)
# f.close()


# 关键字 with

with open(flame,'wb') as f:
    runner = HTMLTestRunner(f, title='报告', description='v1.0')
    runner.run(suite)



