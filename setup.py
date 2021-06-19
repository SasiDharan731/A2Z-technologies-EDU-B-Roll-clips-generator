from setuptools import setup
setup(
    name = 'Broll_generator',
    version = '0.1.0',
    packages = ['Broll_generator'],
    entry_points = {
        'console_scripts': [
            'Broll_generator = Broll_generator.__main__:main'
        ]
    })