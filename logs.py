import os
class Log:
    def __init__(self):
        self.file_name = os.getenv('LOG_PATH')
    def write(self, text):
        if os.getenv('LOGS') == "1":
            file = open(self.file_name, "a+")
            file.write(text + '\n')
            file.close()