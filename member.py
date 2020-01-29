import sys, os, subprocess

def main():
	help_msg = lambda: print(
		'Member v0.2.0 - Timed Messagebox Reminders\n'
		'Note: Reminders do not persist after reboot\n'
		'Usage: member <waiting period> <message>\n'
		'       member -h | --help'
	)

	format_msg = lambda: print(
		'Waiting Period Format:\n'
		'       Seconds: 1s 60s 90s\n'
		'       Minutes: 1m 1.387m 90m\n'
		'       Hours:   1h 1.5h 0.33h'
	)

	if len(sys.argv) < 3:
		if '-h' in sys.argv or '--help' in sys.argv:
			format_msg()
		else:
			help_msg()
		exit()

	_, wait, message = sys.argv

	durations = {'s' : 1, 'm' : 60, 'h' : 60 * 60}

	if wait[-1] not in durations:
		print(f'Error: Invalid waiting period format.\n')
		format_msg()
		exit()

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
