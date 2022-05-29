from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/Rathore2014/tutorial-pip-package',
    author='Rajiv Singh',
    author_email='rajmca.rajiv@gmail.com',

    py_modules=['my_pip_package'],
)