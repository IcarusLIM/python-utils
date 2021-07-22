from datetime import datetime
import time


class FragementFile:
    def __init__(self, file_name, mode, interval=10, time_format="%Y%m%d%H%M%S"):
        self.file_name = file_name
        self.mode = mode
        self.interval = interval
        self.time_format = time_format

    def __enter__(self):
        self.time = time.time()
        self.file = open(self._get_file_name(), self.mode)
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("exit")

    def write(self, line):
        self._check_interval()
        self.file.write(line)

    def writelines(self, lines):
        self._check_interval()
        self.file.writelines(lines)

    def flush(self):
        self.file.flush()

    def _get_file_name(self):
        return self.file_name + "." + datetime.now().strftime(self.time_format)

    def _check_interval(self):
        if time.time() - self.time > self.interval:
            self.time = time.time()
            self.file.close()
            self.file = open(self._get_file_name(), self.mode)


def open_fragement(*args, **kwargs):
    return FragementFile(*args, **kwargs)
