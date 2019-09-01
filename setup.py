from setuptools import setup

setup(
    name='Reportity',
    url='https://github.com/fnatanoy/reportity',
    author='Yonatan Faigenbaum',
    author_email='fnatanoy@gmail.com',
    packages=['reportity'],
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        '-e git://github.com/mpld3/mpld3@master#egg=mpld3',
        'Jinja2 == 2.10.1',
    ],
    version='0.1',
    license='MIT',
    description='',
    long_description=open('README.md').read(),
)
