from setuptools import setup, find_packages

setup(
    name='dict-toolkit',
    version='0.0.1',
    packages=find_packages(),
    package_dir={'': 'dict-toolkit'}, 
    package_data={
        'e-dict': ['dict/*.csv'],
    },
    include_package_data=True,
    install_requires=[],
)

