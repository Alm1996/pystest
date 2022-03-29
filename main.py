import time
from pywinauto.application import Application

# #启动并创建一个实例对象
# app = Application(backend="uia").start(r'C:\Users\李子元\Desktop\客户端\IMSPlatformClientMod.exe')
# #选中登录窗口
# win_login = app.window(class_name='IMSLogin')
# '''
# # 判断是否为dialog,一个微信是一个dialog，就是窗口
# print(win_login.is_dialog)
# # 给控件画个红色框便于看出是哪个
# win_login.draw_outline(colour = 'red')
# # 打印当前窗口的所有controller（控件和属性）
# win_login.print_control_identifiers(depth = None, filename = None)
# '''
# # 定位登录窗口下的userid，输入账号
# win_userid = win_login.children()[2]
# win_userid.type_keys('^a').type_keys('0000000000000000', with_spaces=True)
# # 定位登录窗口下的password，输入密码
# win_password = win_login.children()[4]
# win_password.type_keys('{TAB}').type_keys('123', with_spaces=True)
# # 定位登录窗口下的登录按钮，点击登录
# win_login_button = win_login.children()[5]
# win_login_button.click()

app = Application(backend="uia").connect(path=r"C:\Users\李子元\Desktop\客户端\IMSPlatformClientMod.exe")
QMainWindow = app.window(class_name='QMainWindow')
#QMainWindow.print_control_identifiers(depth = None, filename = None)
QMainWindow_button = QMainWindow.children()[0].children()[0]
QMainWindow_button.draw_outline(colour = 'red')

