from web_framework.application_container import AppContainer
from controller.controller import *

if __name__ == '__main__':
    app = AppContainer()
    app.routes(
        path='/',
        controller=HomeController()
    )
    app.routes(
        path='/login',
        controller=LoginController()
    )
    app.routes(
        path='/todos',
        controller=ToDoController()
    )
    app.routes(
        path='/else',
        controller=NotFoundController()
    )
    app.run()
