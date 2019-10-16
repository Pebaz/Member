import sys

def main():
	if len(sys.argv) < 3:
		print('Member v0.1.0 - Timed Messagebox Reminders')
		print('Usage: member <minutes> <message>')
		exit()

	_, seconds, message = sys.argv

	# Windows
	if sys.platform == 'win32':
		import subprocess

		command = (
			f'import time, tkinter.messagebox; '
			f'time.sleep({seconds}); '
			f'root = tkinter.Tk(); '
			f'root.withdraw(); '
			f'tkinter.messagebox.showwarning("Member?", {repr(message)})'
		)

		subprocess.Popen(['pythonw', '-c', command])

	# *Nix platforms
	else:
		import os
		n = os.fork()
		if n == 0:
			import time, tkinter.messagebox
			time.sleep({seconds})
			root = tkinter.Tk()
			root.withdraw()
			tkinter.messagebox.showwarning("Member?", {repr(message)})
