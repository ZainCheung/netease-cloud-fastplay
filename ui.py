# -*- coding: utf-8 -*- 

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"网易云音乐个性化纠正工具", pos = wx.DefaultPosition, size = wx.Size( 500,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
        
        conf = self.initData()
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.Text_account = wx.StaticText( self, wx.ID_ANY, u"账号", wx.Point( -1,-1 ), wx.Size( 50,-1 ), 0 )
        self.Text_account.Wrap( -1 )
        self.Text_account.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )

        gbSizer1.Add( self.Text_account, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Ctrl_account = wx.TextCtrl( self, wx.ID_ANY, conf['uin'], wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        self.Ctrl_account.SetToolTip( u"手机号或者邮箱" )
        self.Ctrl_account.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Ctrl_account, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Text_api = wx.StaticText( self, wx.ID_ANY, u"API", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_api.Wrap( -1 )
        self.Text_api.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Text_api, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Ctrl_api = wx.TextCtrl( self, wx.ID_ANY, conf['api'], wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        self.Ctrl_api.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Ctrl_api, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Text_id = wx.StaticText( self, wx.ID_ANY, u"歌单ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_id.Wrap( -1 )
        self.Text_id.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Text_id, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Ctrl_id = wx.TextCtrl( self, wx.ID_ANY, conf['id'], wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        self.Ctrl_id.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Ctrl_id, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Text_time = wx.StaticText( self, wx.ID_ANY, u"播放次数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_time.Wrap( -1 )
        self.Text_time.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Text_time, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Ctrl_time = wx.TextCtrl( self, wx.ID_ANY, conf['time'], wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        self.Ctrl_time.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Ctrl_time, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.button_start = wx.Button( self, wx.ID_ANY, u"开始执行", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
        self.button_start.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        self.button_start.SetBackgroundColour( wx.Colour( 0, 181, 46 ) )
        
        gbSizer1.Add( self.button_start, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Text_password = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_password.Wrap( -1 )
        self.Text_password.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        gbSizer1.Add( self.Text_password, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        self.Ctrl_password = wx.TextCtrl( self, wx.ID_ANY, conf['pwd'], wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_PASSWORD )
        self.Ctrl_password.SetFont( wx.Font( 12, 70, 90, 92, False, "微软雅黑" ) )
        self.Ctrl_password.SetToolTip( u"必须填写MD5" )
        
        gbSizer1.Add( self.Ctrl_password, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 20 )
        
        
        self.SetSizer( gbSizer1 )
        self.Layout()
        self.statusBar = self.CreateStatusBar( 1, 0, wx.ID_ANY )
        self.statusBar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        self.menubar = wx.MenuBar( 0 )
        self.menu_file = wx.Menu()
        self.menuItem_openlog = wx.MenuItem( self.menu_file, wx.ID_ANY, u"查看日志", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.menuItem_openlog )
        
        self.menuItem_openconfig = wx.MenuItem( self.menu_file, wx.ID_ANY, u"查看配置", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.menuItem_openconfig )
        
        self.menubar.Append( self.menu_file, u"文件" ) 

        self.menu_function = wx.Menu()
        self.menuItem_getApi = wx.MenuItem( self.menu_function, wx.ID_ANY, u"获取API", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_function.Append( self.menuItem_getApi )
        
        self.menuItem_autoUp = wx.MenuItem( self.menu_function, wx.ID_ANY, u"自动升级", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_function.Append( self.menuItem_autoUp )
        
        self.menubar.Append( self.menu_function, u"功能" ) 
        
        self.menu_help = wx.Menu()
        self.menuItem_about = wx.MenuItem( self.menu_help, wx.ID_ANY, u"关于软件", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_help.Append( self.menuItem_about )
        
        self.menuItem_readme = wx.MenuItem( self.menu_help, wx.ID_ANY, u"使用说明", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_help.Append( self.menuItem_readme )
        
        self.menu_help.AppendSeparator()
        
        self.menuItem_feedback = wx.MenuItem( self.menu_help, wx.ID_ANY, u"反馈问题", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_help.Append( self.menuItem_feedback )

        self.menubar.Append( self.menu_help, u"帮助" ) 
        
        self.SetMenuBar( self.menubar )
        
        
        self.Centre( wx.BOTH )
    
        # Connect Events
        self.button_start.Bind( wx.EVT_LEFT_DOWN, self.start )
        self.Bind( wx.EVT_MENU, self.Event_openlog, id = self.menuItem_openlog.GetId() )
        self.Bind( wx.EVT_MENU, self.Event_openconfig, id = self.menuItem_openconfig.GetId() )
        self.Bind( wx.EVT_MENU, self.Event_getApi, id = self.menuItem_getApi.GetId() )
        self.Bind( wx.EVT_MENU, self.Event_autoUp, id = self.menuItem_autoUp.GetId() )
        self.Bind( wx.EVT_MENU, self.Event_about, id = self.menuItem_about.GetId() )
        self.Bind( wx.EVT_MENU, self.Event_readme, id = self.menuItem_readme.GetId() )
        self.Bind( wx.EVT_MENU, self.Event_feedback, id = self.menuItem_feedback.GetId() )

    def initData( self ):
        conf = {
            'uin': '测试账号',
            'pwd': '',
            'api': '',
            'id': '',
            'time': ''
        }
        return conf
    
    def __del__( self ):
        pass
    
    def Tipmsgbox(self, content): 
        wx.MessageBox(content, "提示" ,wx.OK | wx.ICON_INFORMATION)

    # Virtual event handlers, overide them in your derived class
    def start( self, event ):
        event.Skip()
    
    def Event_openlog( self, event ):
        event.Skip()
    
    def Event_openconfig( self, event ):
        event.Skip()
    
    def Event_getApi( self, event ):
        event.Skip()
    
    def Event_autoUp( self, event ):
        event.Skip()
    
    def Event_about( self, event ):
        event.Skip()
    
    def Event_readme( self, event ):
        event.Skip()
    
    def Event_feedback( self, event ):
        event.Skip()

class Dialog_about ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"关于软件", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.Text_aboutSoft = wx.StaticText( self, wx.ID_ANY, u"本软件开源免费，请勿二次售卖！\n首发：吾爱破解论坛\n作者：ZainCheung(superBoyJack)\n\n声明：本软件仅用于个人学习开发测试，\n所有网易云相关字样版权属于网易公司，\n勿用于商业及非法用途！\n\n如您使用该软件即你已了解并同意该声明！", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_aboutSoft.Wrap( -1 )
        self.Text_aboutSoft.SetFont( wx.Font( 15, 70, 90, 90, False, "微软雅黑" ) )
        
        gbSizer2.Add( self.Text_aboutSoft, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 30 )
        
        self.button_about_know = wx.Button( self, wx.ID_ANY, u"我已了解", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.button_about_know.SetFont( wx.Font( 15, 70, 90, 90, False, "微软雅黑" ) )

        gbSizer2.Add( self.button_about_know, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 30 )
        
        
        self.SetSizer( gbSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.button_about_know.Bind( wx.EVT_BUTTON, self.Event_know )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def Event_know( self, event ):
        self.Destroy()
    
class Dialog_readme ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"使用帮助", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.staticline_readme = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        gbSizer3.Add( self.staticline_readme, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
        
        self.Text_readme_alert = wx.StaticText( self, wx.ID_ANY, u"功能介绍：填入账号密码与API，输入歌单ID和播放次数\n程序会登陆该账号将该歌单播放你指定的次数\n\n提示：播放完成速度取决于你的API速度\n建议播放次数不要太大，效果请到网易云个人主页查看\n\n注意：密码必须自己前往MD5加密网站进行转换\n本软件不会将你的原文密码上传到服务器，请放心使用\n如果API不可用或者速度非常慢请更换\n执行任务之前请不要打开或者删除日志文件和配置文件\n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_readme_alert.Wrap( -1 )
        self.Text_readme_alert.SetFont( wx.Font( 12, 70, 90, 90, False, "微软雅黑" ) )
        
        gbSizer3.Add( self.Text_readme_alert, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 30 )
        
        self.Text_readme_read = wx.StaticText( self, wx.ID_ANY, u"这款软件的开发初衷是为了帮助使用过网易云自动升级的用户\n在系统推送不够精准的情况下进行自我纠正\n通过增加某几首歌的播放次数可以告知系统你的听歌偏好\n以便系统为你推荐你喜欢的歌单以及歌曲", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Text_readme_read.Wrap( -1 )
        self.Text_readme_read.SetFont( wx.Font( 12, 70, 90, 90, False, "微软雅黑" ) )
        
        gbSizer3.Add( self.Text_readme_read, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 30 )
        
        
        self.SetSizer( gbSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    