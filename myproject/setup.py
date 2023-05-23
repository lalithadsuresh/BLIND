from setuptools import setup, find_packages

setup(
    name='myproject',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'django',
        # Add other dependencies here
    ],
    # Add other configuration options as needed
)