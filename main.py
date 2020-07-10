# -*- coding: utf-8 -*-
'''
@author: ZainCheung
@LastEditors: ZainCheung
@description:网易云音乐刷单曲播放次数
@Date: 2020-07-09
@LastEditTime: 2020-07-10
'''

import webbrowser
from threading import Timer
import re
import wx
import os

#导入ui.py,api.py中内容
import ui
import api



class mainWin(ui.MainFrame):
    '''
    创建mainWin类并传入main.MyFrame作为父类
    '''
    def start(self, event):
        '''
        事件函数:开始执行按钮
        '''
        conf = {
            'uin': self.Ctrl_account.GetValue(),
            'pwd': self.Ctrl_password.GetValue(),
            'api': self.Ctrl_api.GetValue(),
            'id': self.Ctrl_id.GetValue(),
            'time': self.Ctrl_time.GetValue()
        }
        if self.check() is True:
            api.save(conf)
            self.conf = conf
            self.button_start.SetLabel("正在执行中...")
            self.button_start.Enable( False )
            Timer(0, self.taskPool, ()).start()
        else:
            pass

    def Event_openlog( self, event ):
        '''
        事件函数:菜单-查看日志
        '''
        os.system('notepad ' + api.path_log)

    def Event_openconfig( self, event ):
        '''
        事件函数:菜单-查看配置
        '''
        os.system('notepad ' + api.path_config)

    def Event_getApi( self, event ):
        '''
        事件函数:菜单-获取api
        '''
        webbrowser.open('https://github.com/ZainCheung/netease-cloud-api')

    def Event_autoUp( self, event ):
        '''
        事件函数:菜单-自动升级
        '''
        webbrowser.open('https://www.52pojie.cn/thread-1208644-1-1.html')

    def Event_about( self, event ):
        '''
        事件函数:菜单-关于软件
        '''
        panel_about = ui.Dialog_about(None).Show()

    def Event_readme( self, event ):
        '''
        事件函数:菜单-使用帮助
        '''
        panel_readme = ui.Dialog_readme(None).Show()

    def Event_feedback( self, event ):
        '''
        事件函数:菜单-反馈问题
        '''
        webbrowser.open('https://github.com/ZainCheung/netease-cloud-fastplay/issues/new')
    
    def initData(self):
        '''
        初始化界面数据
        '''
        conf = api.init()
        return conf

    
    def check(self):
        '''
        检验输入数据的合法性
        '''
        account = self.Ctrl_account.GetValue()
        password = self.Ctrl_password.GetValue()
        api = self.Ctrl_api.GetValue()
        id = self.Ctrl_id.GetValue()
        time = self.Ctrl_time.GetValue()

        state_account = False
        state_password = False
        state_api = False
        state_id = False
        state_time = False

        com_phone = r'[1]+[\d]{10}$'
        com_email = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        com_password = r'[abcdef\d]{32}$'
        com_id = r'[\d]{4,12}$'
        com_time = r'[\d]{1,5}$'

        if(account == ''):
            self.Tipmsgbox('账号不能为空')
        elif ('@' not in account):
            if not re.match(com_phone, account):
                self.Tipmsgbox('手机号格式不正确')
            else:
                state_account = True
        elif not re.match(com_email, account):
            self.Tipmsgbox('邮箱格式不正确')
        else:
            state_account = True

        if not re.match(com_password, password):
            self.Tipmsgbox('密码格式不正确,请将你的密码转换为32位小写的MD5')
        else:
            state_password = True

        if api.startswith('https://') or api.startswith('http://'):
            state_api = True
        else:
            self.Tipmsgbox('API格式不正确,应该以"https://"或者"http://"开头')

        if not re.match(com_id, id):
            self.Tipmsgbox('歌单id格式不正确,应为10位数字,请前往网易云网站查看歌单ID')
        else:
            state_id = True

        if not re.match(com_time, time):
            self.Tipmsgbox('播放格式不正确,应为1至99999之间的整数数字')
        else:
            state_time = True

        if state_account and state_password and state_api and state_id and state_time:
            return True
        else:
            return False

    
    def taskPool(self):
        '''
        任务池
        '''
        task = api.Task(self.conf)
        self.statusBar.SetStatusText(task.login())
        try:
            if task.state is True:
                self.statusBar.SetStatusText(task.listen())
        except:
            pass
        self.button_start.SetLabel("执行完毕")
        self.button_start.Enable( True )

'''
程序主入口
'''
if __name__ == '__main__':
    app = wx.App()
    main_win = mainWin(None)
    main_win.Show()
    app.MainLoop()
