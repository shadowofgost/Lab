
from tornado.web import Application
from tornado import ioloop
import os
from Views.select import SettingsHandler,IndexHandler,SelectHandler
app = Application(
    [(r"/", SettingsHandler),
     (r"/index", IndexHandler),
     (r"/select", SelectHandler)],
    static_path=os.path.join(os.path.dirname(__file__), "Static"),
    template_path=os.path.join(os.path.dirname(__file__), "Templates"),
)
app.listen(8080)
ioloop.IOLoop.instance().start()
