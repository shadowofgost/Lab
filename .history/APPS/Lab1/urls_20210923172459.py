'''
Author: your name
Date: 2021-09-20 09:51:59
LastEditTime: 2021-09-23 17:14:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Lab\APPS\Lab1\urls.py
'''
from tornado.web import Application
from tornado import ioloop
import os
from Views.select import SettingsHandler
app = Application(
    [(r"/", SettingsHandler),
     ],
    static_path=os.path.join(os.path.dirname(__file__), "Static"),
    template_path=os.path.join(os.path.dirname(__file__), "Templates"),
)
app.listen(8080)
ioloop.IOLoop.instance().start()
