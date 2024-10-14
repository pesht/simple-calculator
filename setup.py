from setuptools import setup, find_packages

setup(
    name='simple_calculator',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'selenium==4.25.0',
        'webdriver_manager==4.0.2',
        'requests==2.26.0',
    ],
)
