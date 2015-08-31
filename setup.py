"""Set up biicode as a proper module
"""

# We will use setuptools
from setuptools import setup, find_packages

setup(
    name='biicode',
    version='3.3',

    description='C/C++ Dependency Manager',
    long_description=('Biicode is a C/C++ dependency manager and associated '
        'cloud service for publishing "blocks".'),

    url='http://biicode.github.io/biicode/',

    author='Biicode',
    # TODO: e-mail

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: C++',
        'Programming Language :: C'
    ],

    keywords='biicode dependency management',
    packages=find_packages(),

    
    install_requires=['python-graph-core>=1.8.2', 'pytz>=2013b', 'pyyaml>=3.10', 
        'ply', 'pymongo>=2.7', 'pyserial', 'jinja2>=2.7.2', 'colorama>=0.2.7',
        'requests>=2.2.1'],
        
    # $ pip install -e .[server]
    extras_require={
        'server': ['wsgiref==0.1.2', 'passlib==1.6.1', 'bottle==0.12.7',
            'bottle-memcache==0.2', 'python-memcached==1.48', 'pylibmc',
            'newrelic', 'gevent==0.13.8', 'greenlet==0.4.0', 'gunicorn==0.17.2',
            'rq==0.3.8', 'Delorean==0.3.1', 'PyJWT==0.2.1', 'mandrill==1.0.53',
            'mixpanel-py==3.2.1', 'mixpanel-py-async==0.0.5',
            'google-measurement-protocol==0.1.3', 'pycrypto==2.6.1',
            'stripe==1.20.2']
    },

    # TODO: Modify bii's main not to need arguments, and use entry_points
    # instead. For now we use the provided bii script even though it messes
    # about with the python path.
    scripts=['biicode/bii']
)

