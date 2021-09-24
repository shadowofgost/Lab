'''
Author: your name
Date: 2021-09-20 10:52:09
LastEditTime: 2021-09-23 15:51:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Lab\APPS\Lab1\Views\select.py
'''
from tornado.web import RequestHandler
class SelectHandler(RequestHandler):
    def get(self):
        self.render('select.html')
    def post(self):
        self.render('select.html')
