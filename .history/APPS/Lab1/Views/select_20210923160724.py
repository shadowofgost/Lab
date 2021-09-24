'''
Author: your name
Date: 2021-09-20 10:52:09
LastEditTime: 2021-09-23 16:06:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Lab\APPS\Lab1\Views\select.py
'''
from tornado.web import RequestHandler
from random import randint
class SelectHandler(RequestHandler):
    def get(self):
        self.render('select.html')
    def post(self):
        prize_number = int(self.get_argument('prize_number'))
        prize_number_list = {}
        for i  in range(1,prize_number+1):
            tmp = int(self.get_argument('prize_'+str(i)))
            prize_number_list[i] = tmp
        participant_list = self.get_argument('participant').split(';')
        participant_number = len(participant_list)-1
        