import sys, subprocess

def main():
	if len(sys.argv) < 3:
		print('Member v0.1.0 - Timed Messagebox Reminders')
		print('Usage: member <minutes> <message>')
		exit()

	_, seconds, message = sys.argv

	command = (
		f'import time, tkinter.messagebox; '
		f'time.sleep({seconds}); '
		f'root = tkinter.Tk(); '
		f'root.withdraw(); '
		f'root.lift(); '
		f'root.attributes("-topmost", True); '
		f'tkinter.messagebox.showwarning("Member?", {repr(message)})'
	)

	python = 'python' if sys.platform == 'win32' else 'python3'
	subprocess.Popen([python, '-c', command])
