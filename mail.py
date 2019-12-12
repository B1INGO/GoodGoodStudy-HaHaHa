import yagmail
from sys import exit
# 基类
class Account_Infor:
    '''已完成：此处 处理账号密码'''
    def __init__(self, argu):
        try:
            print(argu)
            self.__account, self.__password = argu
            print('Account:'+self.__account + '\n' + 'Password:' + self.__password)
        except:
            print("变量解包出现错误")
            exit()
        self.__check_format()
    def __check_format(self):
        '''格式检查和修改'''
        print("执行__check_format")
        self.__account = str(self.__account)
        self.__password = str(self.__password)
        # 判断是不是将账号密码输反了
        if ('@' not in self.__account ) and ('@' in self.__password ):
            #账号密码输入错误-->>>已自动纠正
            self.__tmp = self.__account
            self.__account = self.__password
            self.__password = self.__tmp
            print('Account:'+self.__account + '\n' + 'Password:' + self.__password)
            self.a = self.__account
            self.p = self.__password

class Tian_Email():
    '''脚本出口'''
    def __init__(self, *argu):
        self.__account = Account_Infor(argu)
        self.__email_type()
    def __email_type(self):
        # 配置邮箱smpt
        self.email_profies = {"163.com":{'smtp':'smtp.163.com', 'port':465}, "qq.com":{'smtp':'smtp.qq.com', 'port':465}}
        self.__smpt = self.email_profies[self.__account.a.split('@')[-1]]['smtp']
        self.__port = self.email_profies[self.__account.a.split('@')[-1]]['port']        
    def send(self,email,title,contents):
#        try:
            self.__yag = yagmail(self.__account.a, self.__account.p, self.__smtp)
            self.__yag.send(email, title, contents)
#        except:
#            print("邮件发送错误")
def am_function():
    '''测试用'''
    pass
        
if __name__ == '__main__':
    pass