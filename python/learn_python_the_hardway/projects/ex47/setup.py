try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'first automated test',
	'author': 'mfdestiny',
	'url': 'URL to get it at.',
	'download_url': 'http://github.com/mfdestiny',
	'author_email': 'mfdestiny@protonmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'example47_testing'
}
setup(**config)
