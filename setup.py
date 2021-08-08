from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()

longDescription = (here / 'README.md').read_text('utf-8')
description = longDescription.split('\n')[1]

NAME = ''
VERSION = '0.1.0'

setup(
    name=NAME,
    version=VERSION,
    description=description,
    long_description=longDescription,
    long_description_content_type='text/markdown',
    author='Hazel Rella',
    author_email='hazelrella11@gmail.com',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.8, <4',
    install_requires=[

    ],
    entry_points={
        # 'console_scripts': [
        #     'commandName=packageName:functionName'
        # ]
    }
)
