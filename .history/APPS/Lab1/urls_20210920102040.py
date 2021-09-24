from tornado.web import Application
import os
app = Application(
    [(r"/test", TestHandler),
     ],
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
)
