import sys, os, subprocess

def main():
	if len(sys.argv) < 3:
		if '-h' in sys.argv or '--help' in sys.argv:
			print('Waiting Period Format:')
			print('       Seconds: 1s 60s 90s')
			print('       Minutes: 1m 1.387m 90m')
			print('       Hours:   1h 1.5h 0.33h')

		else:
			print('Member v0.2.0 - Timed Messagebox Reminders')
			print('Note: Reminders do not persist after reboot')
			print('Usage: member <waiting period> <message>')
			print('       member -h | --help')

		exit()

	_, wait, message = sys.argv

	durations = {'s' : 1, 'm' : 60, 'h' : 60 * 60}

	for form in durations:
		if form in wait:
			duration, form, _ = wait.partition(form)
			seconds = float(duration) * durations[form]

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


if __name__ == '__main__':
	main()
