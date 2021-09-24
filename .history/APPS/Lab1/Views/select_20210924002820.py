"""
Author: your name
Date: 2021-09-20 10:52:09
LastEditTime: 2021-09-23 17:22:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Lab\APPS\Lab1\Views\select.py
"""
import re
from tornado.web import RequestHandler
from random import randint,random
from json import dumps,loads

class SettingsHandler(RequestHandler):
    def get(self):
        self.render("settings.html")

    def post(self):
        prize_number = int(self.get_argument("prize_number"))
        prize_number_list = {}
        for i in range(1, prize_number + 1):
            tmp = int(self.get_argument("prize_" + str(i)))
            prize_number_list[i] = tmp
        participant_list = self.get_argument("participant").split(";")
        participant_number = len(participant_list) - 1
        random_list = [
            randint(1, participant_number) for i in range(participant_number)
        ]
        result_list = []
        for i in range(1, participant_number + 1):
            tmp = (participant_list[i], random_list[i - 1])
            result_list.append(tmp)
        result_list.sort(key=lambda x: x[1])
        result_return = {}
        for i in result_list:
            sign = 0
            for j in prize_number_list.keys():
                if prize_number_list[j] > 0:
                    sign = 1
                    result_return[i[0]] = str(j) + "等奖"
                    prize_number_list[j] -= 1
                    break
            if sign == 0:
                result_return[i[0]] = "未中奖"
        self.render("result.html", result_return=result_return)


class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self):
        prize_number = int(self.get_argument("prize_number"))
        prize_number_list = []
        prize_random_list = []
        for i in range(1, prize_number + 1):
            tmp = str(self.get_argument("prize_" + str(i)))
            prize_number_list.append(tmp)
            tmp = str(self.get_argument("prize_random_" + str(i)))
            prize_random_list.append(tmp)
        result_return = ["测试;用例","测试;用例"]
        print_results ="测试"
        result ={}
        for i in range(len(result_return)):
            result[result_return[i].split(";")[0]] = result_return[i].split(";")[1]
        self.set_cookie("prize_number", str(prize_number))
        self.set_cookie("prize_number_list", ",".join(prize_number_list))
        self.set_cookie("prize_random_list",",".join(prize_random_list))
        self.render("select.html",result_return=result,print_results=print_results,data =','.join(result_return))

class SelectHandler(RequestHandler):
    def get(self):
        self.render("select.html")
    def post(self):
        prize_number = int(self.get_cookie("prize_number"))
        prize_number_list = self.get_cookie("prize_number_list").split(",")
        prize_random_list = self.get_cookie("prize_random_list").split(",")
        result_return = self.get_argument("data").split(",")
        print(result_return)
        name = self.get_argument("name")
        sign_random = random()
        count = 0
        sign = 0
        for i in range(prize_number):
            count += float(prize_random_list[i])
            if sign_random < count:
                if int(prize_number_list[i]) > 0:
                    sign = 1
                    result_return.append(name +";"+ str(i)+"等奖")
                    print_results = name+"获得"+str(i)+"等奖"
                    prize_number_list[i] = str(int(prize_number_list[i]) - 1)
                    break
        if sign == 0:
            result_return.append(name +";"+"未中奖")
            print_results = "未中奖"
        print(result_return)
        result={}
        for i in range(len(result_return)):
            result[result_return[i].split(";")[0]] = result_return[i].split(";")[1]
        self.set_cookie("prize_number", str(prize_number))
        self.set_cookie("prize_number_list", ",".join(prize_number_list))
        self.set_cookie("prize_random_list",",".join(prize_random_list))
        self.set_cookie("result_return",",".join(result_return))
        self.render("select.html",result_return=result,print_results=print_results)
