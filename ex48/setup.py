try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'lexicon',
	'author': 'mfdestiny',
	'url': 'https://www.github.com/mfdestiny',
	'download_url': 'http://github.com/mfdestiny',
	'author_email': 'mfdestiny@protonmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'lexicon'
}
setup(**config)
