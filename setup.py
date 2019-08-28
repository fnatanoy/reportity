from setuptools import setup

setup(
    name='Reportity',
    url='https://github.com/fnatanoy/reportity',
    author='Yonatan Faigenbaum',
    author_email='fnatanoy@gmail.com',
    packages=['reportity'],
    install_requires=[
        'numpy',
        'pandas',
        'mpld3',
    ],
    version='0.1',
    license='MIT',
    description='',
    long_description=open('README.rst').read(),
)
