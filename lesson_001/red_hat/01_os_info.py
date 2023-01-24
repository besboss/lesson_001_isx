# -*- coding: utf-8 -*-

# Нужно собрать инфу об ОС

import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info_v2.txt', 'w') as ff:
    ff.write(info)
