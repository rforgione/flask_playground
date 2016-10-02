from app.views import *

class Controllers_HelloWorldController(object):
    def __init__(self, name):
        self.name = name

    def render_view(self):
        view = Views_HelloWorldView(self.name)
        return view.render()
