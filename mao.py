
import os, platform

bit = platform.architecture()[0]
def __init__():
    if bit == '64bit':
        from mao_main import defultchk
        defultchk()
    else:
        print(bit)
        exit()
__init__()
