from setuptools import setup

setup(
    name='reportity',
    url='https://github.com/fnatanoy/reportity',
    author='Yonatan Faigenbaum',
    author_email='fnatanoy@gmail.com',
    packages=['reportity'],
    install_requires=[
        'matplotlib',
        'mpld3',
        'numpy',
        'pandas',
        # 'Jinja2 == 2.10.1',
    ],
    dependency_links=[
        'git+git://github.com/mpld3/mpld3@master#egg=mpld3',
    ],
    version='0.3',
    license='MIT',
    description='this is the best package for reports',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords=['report','analysis','figures','plot'],
    download_url='https://github.com/fnatanoy/reportity/archive/v_03.tar.gz',
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
