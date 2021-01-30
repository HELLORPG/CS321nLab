import platform
import os


class PythonVersion:
    def __init__(self):
        return

    @staticmethod
    def version(self):
        return platform.python_version()

    def print_(self):
        filename = os.path.basename(__file__)   # 获取当前文件文件名
        print("====> %s: Python Version is" % filename, self.version())


if __name__ == '__main__':
    python_version = PythonVersion()
    python_version.print_()
