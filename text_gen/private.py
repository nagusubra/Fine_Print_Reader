class config():
    def __init__(self):
        self.status = self
        self.openai_API_KEY = ''

    def get_openai_key(self):
        return self.openai_API_KEY