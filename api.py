#coding:utf-8
'''
@author: ZainCheung
@LastEditors: ZainCheung
@description:api模块
@Date: 2020-07-09
@LastEditTime: 2020-07-10
'''
from configparser import ConfigParser
import json
import logging
import os
import requests

current_path = os.getcwd()
path_log = current_path + '\\run.log'
path_config = current_path + '\\init.config'
logFile = open(path_log, encoding="utf-8", mode="a")
logging.basicConfig(stream=logFile, format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

class Task(object):
    '''
    对象的构造函数
    '''
    def __init__(self, conf):
        self.uin = conf['uin']
        self.pwd = conf['pwd']
        self.api = conf['api']
        self.id = conf['id']
        self.time = conf['time']

    def get_response(self, url, post_json):
        '''
        带上用户的cookie去发送数据
        url:完整的URL路径
        postJson:要以post方式发送的数据
        返回response
        '''
        response = requests.post(url, data=post_json, headers={
            'Content-Type':'application/x-www-form-urlencoded'}, cookies=self.cookies)
        return response

    def login(self):
        '''
        登陆函数
        '''
        data = {"uin":self.uin,"pwd":self.pwd}
        if '@' in self.uin:
            url = self.api + '?do=email'
        else:
            url = self.api + '?do=login'
        try:
            response = requests.post(url, data=data, headers={'Content-Type':'application/x-www-form-urlencoded'})
        except:
            logging.error("服务器连接失败,请检查API以及当前网络环境")
            return '服务器连接失败,请检查API以及当前网络环境'
        else:
            code = json.loads(response.text)['code']
            if code==200:
                self.name = json.loads(response.text)['profile']['nickname']
                self.uid = json.loads(response.text)['account']['id']
                self.cookies = response.cookies.get_dict()
                self.error = self.name + '登陆成功!'
                self.state = True
                logging.info(self.name + '登陆成功!')
            else:
                self.state = False
                self.error = '登陆失败，请检查账号密码是否正确'
                logging.error("登陆失败，请检查账号密码是否正确")
            return self.error
        

    '''
    听歌
    '''
    def listen(self):
        url = self.api + '?do=listen'
        data = {"id":self.id, "time":self.time}
        try:
            response = self.get_response(url, data)
            data = json.loads(response.text)
            self.count = data['count']
        except:
            logging.error("听歌失败,请检查API是否为最新版本!")
            return '听歌失败,请检查API是否为最新版本!'
        else:
            logging.info("听歌成功,共听" + str(self.count) + "首")
            return '听歌成功,共听' + str(self.count) + '首'          
        
'''
初始化：读取配置,配置文件为init.config
返回字典类型的配置对象
'''
def init():
    config = ConfigParser()
    config.read(path_config, encoding='UTF-8-sig')
    uin = config.get('token', 'account')
    pwd = config.get('token', 'password')
    api = config.get('setting', 'api')
    id = config.get('setting', 'id')
    time = config.get('setting', 'time')
    conf = {
            'uin': uin,
            'pwd': pwd,
            'api': api,
            'id': id,
            'time': time
        }
    return conf

def save(conf):
    '''
    数据持久化
    '''    
    config = ConfigParser()
    config.read(path_config, encoding='UTF-8-sig')
    config.set("token", "account", conf['uin'])
    config.set("token", "password", conf['pwd'])
    config.set("setting", "api", conf['api'])
    config.set("setting", "id", conf['id'])
    config.set("setting", "time", conf['time'])
    try:
        with open("init.config", "w+") as f:
            config.write(f)
    except ImportError:
        pass
