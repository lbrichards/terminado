"""A single common terminal for all websockets.
"""
import sys
from path import Path
temp = Path("__file__").abspath()
while temp.basename() != "terminado":
    temp = temp.parent
sys.path.append(temp)
print(temp)
from config import SOCKET, shell_cmd
import tornado.web
# This demo requires tornado_xstatic and XStatic-term.js
import tornado_xstatic

from terminado import TermSocket, SingleTermManager
from demos.common_demo_stuff import run_and_show_browser, STATIC_DIR, TEMPLATE_DIR

class TerminalPageHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("termpage.html", static=self.static_url,
                           xstatic=self.application.settings['xstatic_url'],
                           ws_url_path="/websocket")

def main(argv):
    term_manager = SingleTermManager(shell_command=[shell_cmd])
    handlers = [
                (r"/websocket", TermSocket,
                     {'term_manager': term_manager}),
                (r"/", TerminalPageHandler),
                (r"/xstatic/(.*)", tornado_xstatic.XStaticFileHandler,
                     {'allowed_modules': ['termjs']})
               ]
    app = tornado.web.Application(handlers, static_path=STATIC_DIR,
                      template_path=TEMPLATE_DIR,
                      xstatic_url = tornado_xstatic.url_maker('/xstatic/'))
    app.listen(SOCKET, 'localhost')
    run_and_show_browser(f"http://localhost:{SOCKET}/", term_manager)

if __name__ == '__main__':
    main([])