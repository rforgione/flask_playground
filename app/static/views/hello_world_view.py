class Views_HelloWorldView(object):
    TEMPLATE = 'app/assets/html/hello_world.html'

    def __init__(self, name):
        self.name = name

    def render(self):
        return render_template(self.TEMPLATE, {
            "name": self.name
        })
