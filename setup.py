from setuptools import setup, find_packages


setup(
    name='prettylogger',
    version='0.1.0',
    url='http://github.com/arnellebalane/prettylogger',
    license='MIT',
    description='Print lists, dicts, and tuples in color and beautiful format.',
    author='Arnelle Balane',
    author_email='arnellebalane@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    test_suite='prettylogger'
)