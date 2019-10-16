from setuptools import setup

setup(
	name='member',
	version='0.1',
	author='https://github.com/Pebaz',
	py_modules=['member'],
	entry_points={
		'console_scripts' : [
			'member=member'
		]
	}
)
