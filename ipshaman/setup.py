import ipshaman
from setuptools import setup

setup(
    name='ipshaman',
    version=ipshaman.__version__,
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    url='https://github.com/vesche/python_challenge', # TODO: update this
    description='ipshaman cli',
    license='MIT',
    packages=[
        'ipshaman',
        'ipshaman.cli',
        'ipshaman.core',
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'ipshaman=ipshaman.cli:main',
        ],
    },
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        "Intended Audience :: Information Technology",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet",
    ),
)
