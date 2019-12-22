# coding=utf-8
import requests,json


class HTTP:
    def __init__(self):
        self.session = requests.session()
        self.url = ''
        self.jsonres = None
        self.res = None

    def seturl(self,url):
        '''
        :param url: 基本的url地址
        :return:
        '''
        self.url = url

    def post(self,path,params=None):
        '''
        post请求方法
        :param path: 请求路径
        :param params: 请求参数
        :return:
        '''
        self.res = self.session.post(self.url + path,data=self.__get_data(params))
        self.jsonres = json.loads(self.res.text)
        print(self.jsonres)

    def addheader(self,key,value):
        '''
        向session里面添加头
        :param key: 头的健
        :param value: 头的值
        :return:
        '''
        self.session.headers[key] = value

    def __get_data(self,params):
        '''
        将url格式参数转换为字典格式
        :param params: 传入的url参数
        :return: 字典参数
        '''
        if params is None or params == '':
            return None
        else:
            dict_params = {}
            list_params = params.split('&')
            for item in list_params:
                if item.find('=') >= 0:
                    dict_params[item[:item.find('=')]] = item[item.find('=')+1:]
                else:
                    dict_params[item] = None
        return dict_params













