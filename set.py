def setup_for_loggef():
	#Installing packages
	try:
		import os,sys,time,random
		from uuid import getnode
		import platform
		import mysql.connector
		import requests
		from termcolor import colored
		from colorama import Fore,Back,Style
		from bs4 import BeautifulSoup as bs
		print('\033[1;32;40mSetup is already installed!\033[1;0m')
		sys.exit()
	except ModuleNotFoundError:
		def installer():
			try:
				print('\033[1;36;40mWait please, \033[1;31;40mInstalling resources...\033[1;0m')
				pt=platform.uname()[0]
				if pt.lower()=='windows':
					os.system('pip install colorama termcolor requests bs4 mysql mysql-connector')
				elif pt.lower()=='linux':
					os.system('pkg install mariadb && apt install mariadb && apt install python && apt install git && pip install colorama termcolor requests bs4 mysql mysql-connector')
				else:
					print('\033[1;31;40mUnsuported operating system detected, please make sure you are using linux or windows platform..\033[1;0m')
					sys.exit()
			except KeyboardInterrupt:
				sys.exit('\033[1;31;40mN[+] Service killed!\033[1;0m')
		installer()
setup_for_loggef()






