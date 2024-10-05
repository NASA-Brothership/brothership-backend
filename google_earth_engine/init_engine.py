import ee

class GoogleEartnInterface():
    def __init__(self):
        self.init_engine()

    def init_engine():
        ee.Authenticate()
        ee.Initialize(project='my-project')