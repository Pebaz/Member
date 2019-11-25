import sys, os, subprocess

def main():
	if len(sys.argv) < 3:
		print('Member v0.1.0 - Timed Messagebox Reminders')
		print('Usage: member <minutes> <message>')
		exit()

	_, seconds, message = sys.argv

	command = (
		f'import time, os, tkinter.messagebox; '
		f'time.sleep({seconds}); '
		f'root = tkinter.Tk(); '
		f'root.withdraw(); '
		f'root.lift(); '
		f'root.attributes("-topmost", True); '
	)

	if sys.platform == 'darwin':
		command += """os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' '''); """

	command += f'tkinter.messagebox.showwarning("Member?", {repr(message)})'

	python = 'python' if sys.platform == 'win32' else 'python3'
	subprocess.Popen([python, '-c', command])
