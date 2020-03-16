from setuptools import setup, find_packages

name = 'pyhigh'
version = '0.0.5'

DESCRIPTION = '''\
Python library to get elevation data\
'''

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=name,
    version=version,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords = ['elevation'],
    packages=find_packages(exclude=['tests']),
    entry_points = {
        'console_scripts': [
            'pyhigh=pyhigh.pyhigh:main'
        ]
    },
    install_requires=[
        'numpy',
        'requests'
    ],
    license='MIT',
    url=f'https://github.com/sgherbst/{name}',
    author='Steven Herbst',
    author_email='sherbst@stanford.edu',
    python_requires='>=3.7',
    download_url = f'https://github.com/sgherbst/{name}/archive/v{version}.tar.gz',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    include_package_data=True,
    zip_safe=False
)
