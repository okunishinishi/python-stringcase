from distutils.core import setup

setup(
    name='stringcase',
    version='1.2.0',
    py_modules=[
        'stringcase'
    ],
    url='https://github.com/okunishinishi/python-stringcase',
    license='MIT',
    author='Taka Okunishi',
    author_email='okunishitaka.com@gmail.com',
    description='String case converter.',
    long_description=open('./README.rst').read()
)
