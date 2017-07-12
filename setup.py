from setuptools import setup

setup(
    name='ravenpackapi',
    version='0.3.2',
    packages=['ravenpackapi'],
    url='https://github.com/RavenPack/python-api',
    license='MIT',
    author='RavenPack',
    author_email='dvarotto@ravenpack.com',
    description='RavenPack API - Python client',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='python analytics api rest news data',
    install_requires=['requests[security]'],
)
