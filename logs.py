import os
class Log:
    def __init__(self):
        self.file_name = os.getenv('LOG_PATH')
    def write(self, text):
            file = open(self.file_name, "a+")
            file.write(text + '\n')
            file.close()