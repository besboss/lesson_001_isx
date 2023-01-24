# -*- coding: utf-8 -*-

# Нужно собрать инфу об ОС

# добавил эту строку

import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
