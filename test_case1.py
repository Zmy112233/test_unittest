
from controller import login

assert "登录成功" == login('admin','123456')
assert "用户名为空" == login('','123456')
assert "密码为空" == login('admin','')