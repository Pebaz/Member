from setuptools import setup

setup(
	name='member',
	version='0.2.0',
	author='https://github.com/Pebaz',
	py_modules=['member'],
	entry_points={
		'console_scripts' : [
			'member=member:main'
		]
	}
)
