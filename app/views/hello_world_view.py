from flask import render_template

class Views_HelloWorldView(object):
    TEMPLATE = 'hello_world.html'

    def __init__(self, name):
        self.name = name

    def render(self):
        template_vars = {
            "name": self.name
        }
        return render_template(self.TEMPLATE, **template_vars)
