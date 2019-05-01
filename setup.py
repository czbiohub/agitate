import os, glob
from setuptools import setup

install_requires = [line.rstrip() for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))]

setup(
    name="agitate",
    version="0.1",
    url='https://github.com/czbiohub/agitate',
    license=open("LICENSE").readline().strip(),
    author='agitate contributors',
    author_email='bdimitrov@chanzuckerberg.com',
    description='Developer productivity tools that help blend the power of dev servers with the ligthness of local laptop editing.',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    extras_require={},
    packages=None,
    package_dir=None,
    scripts=glob.glob('scripts/*'),
    data_files=None,
    platforms=['MacOS X', 'Posix'],
    zip_safe=False,
    test_suite=None,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
