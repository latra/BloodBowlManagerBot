class Log:
    def __init__(self):
        self.file_name = "logs"
    def write(self, text):
        file = open(self.file_name, "x")
        file.write(text + '\n')