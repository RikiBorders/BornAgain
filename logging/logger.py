
class Logger:
    def __init__(self, name):
        self.name = name

    def log_info(self, message):
        print(f"[{self.name}][INFO] {message}")

    def log_error(self, message):
        print(f"[{self.name}][ERROR] {message}")

    def log_warn(self, message):
        print(f"[{self.name}][WARN] {message}")