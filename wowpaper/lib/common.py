import os.path
from sys import platform
from os import system
import ctypes


def set_wallpaper(path) -> (bool, str):
    r"""
    setting wallpaper by the path of image
    :param path: the path of image
    :return: None
    """
    if not os.path.exists(path):
        return False, 'File does not exits!'
    if platform.__contains__('win32'):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        return True, 'Success'
    elif platform.lower().__contains__('darwin'):
        cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"%s\"'" % path
        system(cmd)
        return True, 'Success'
    else:
        return False, 'The operating system you are using does not support it yet!'


if __name__ == '__main__':
    set_wallpaper('C:\\Users\\Xuan Ronaldo\\Desktop\\DSC02216.jpg')
