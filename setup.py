from setuptools import setup

setup(
    name='reportity',
    url='https://github.com/fnatanoy/reportity',
    author='Yonatan Faigenbaum',
    author_email='fnatanoy@gmail.com',
    packages=['reportity'],
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'Jinja2 == 2.10.1',
    ],
    dependency_links=[
        'git+git://github.com/mpld3/mpld3@master#egg=mpld3',
    ],
    version='0.2',
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    keywords=['report','analysis','figures','plot'],
    download_url='https://github.com/fnatanoy/reportity/archive/v_021.tar.gz',
)
