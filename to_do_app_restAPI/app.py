from web_framework.application_container import AppContainer
from controller import *

if __name__ == '__main__':
    app = AppContainer()
    app.routes(
        path='/',
        controller=ToDoController()
    )
    app.run()
