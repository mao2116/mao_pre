
import os, platform

bit = platform.architecture()[0]
def mao_main():
    if bit == '64bit':
        from mao_main import defultchk
        defultchk()
    '''elif bit == '32bit':
        from fuck_mao_32 import menu
        menu()'''
    else:
        print(bit)
        exit()
