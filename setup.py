from setuptools import setup, find_packages

setup(
    name="quick-summarize-documents-20260507_200503",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'quick=quick:main',
        ],
    },
)
