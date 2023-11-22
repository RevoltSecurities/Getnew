from setuptools import setup, find_packages

setup(
    name='getnew',
    version='1.0.0',
    author='D. Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description='Getnew tool to get unique line',
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.4'
    ],
    entry_points={
        'console_scripts': [
            'getnew = getnew.getnew:main'
        ]
    },
)