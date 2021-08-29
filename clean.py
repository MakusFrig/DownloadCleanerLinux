'''
This is the file cleaner on python
'''

import os

import sys


def linux_main():
	files = os.listdir()

	#We should try to make folders if they are not there

	for each_file in files:

		if each_file.__contains__('.pdf'):

			if os.path.isfile('~/Documents/PDFS'):

				os.system(f'mv \'{each_file}\' ~/Documents/PDFS')

			else:

				os.system('mkdir ~/Documents/PDFS')

				os.system(f'mv \'{each_file}\' ~/Documents/PDFS')

		elif '.jpg' in each_file or '.png' in each_file or '.jpeg' in each_file:

			os.system(f'mv \'{each_file}\' ~/Pictures')

		elif '.txt' in each_file or '.docx' in each_file:

			os.system(f'mv \'{each_file}\' ~/Documents')

		elif '.mp3' in each_file or '.m4a' in each_file or '.wav' in each_file:

			os.system(f'mv \'{each_file}\' ~/Music')

		elif '.mp4' in each_file:

			os.system(f'mv \'{each_file}\' ~/Videos')

		elif '.py' in each_file:

			if os.path.isfile('~/Documents/PYTHON'):

				os.system(f'mv {each_file} ~/Documents/PYTHON')

			else:

				os.system('mkdir ~/Documents/PYTHON')

				os.system(f'mv {each_file} ~/Documents/PYTHON')

		elif '.c' in each_file:

			if os.path.isfile('~/Documents/C'):

				os.system(f'mv {each_file} ~/Documents/C')

			else:

				os.system('mkdir ~/Documents/C')

				os.system(f'mv {each_file} ~/Documents/C')

		elif '.java' in each_file:

			if os.path.isfile('~/Documents/JAVA'):

				os.system(f'mv {each_file} ~/Documents/JAVA')

			else:

				os.system('mkdir ~/Documents/JAVA')

				os.system(f'mv {each_file} ~/Documents/JAVA')

		elif '.html' in each_file or '.css' in each_file or '.js' in each_file:

			if os.path.isfile('~/Documents/WEB'):

				os.system(f'mv {each_file} ~/Documents/WEB')

			else:

				os.system('mkdir ~/Documents/WEB')

				os.system(f'mv {each_file} ~/Documents/WEB')

		elif '.' not in each_file:
			#WE have found a folder

			os.system(f'mv {each_file} ~/Desktop')

		else:

			if os.path.isfile('~/Documents/MISC'):

				os.system(f'mv {each_file} ~/Documents/MISC')

			else:

				os.system('mkdir ~/Documents/MISC')

				os.system(f'mv {each_file} ~/Documents/MISC')
if len(sys.argv) == 2:
	#we want to use this as the directory

	pass


if sys.platform == 'linux':

	linux_main()


	