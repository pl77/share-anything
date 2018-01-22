from setuptools import setup

setup(
    name='share-anything',
    version='0.0.1',
    packages=['share', 'share.hosts'],
    scripts=[],
    entry_points = { 'console_scripts': ['share=share.__main__:main']},
    install_requires=[
        'certifi>=2017.4.17',
        'chardet>=3.0.4',
        'idna>=2.5',
        'requests>=2.18.1',
        'urllib3>=1.21.1'
    ],

    test_suite='test',

    author='Adithya Reddy',
    author_email='dithyakreddy6@gmail.com',
    url='http://github.com/tallpants/share-anything',
    license='GPLv3',
    description='Share any file type with one command',
    long_description=open('README.md').read(),
    classifiers=['Development Status :: 3 - Alpha',
                 ('License :: OSI Approved :: ' +
                  'GNU General Public License v3 (GPLv3)')]
)
