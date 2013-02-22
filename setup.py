from distutils.core import setup

setup(
    name='CapLocationFinder',
    version='0.1.0',
    author='Patrick Aubin',
    author_email='patrick@capacitr.com',
    packages=['cap_location'],
    url='http://capacitr.com/',
    description='A simple location finder in django and tastypie.',
    install_requires=[
        'django-tastypie==0.9.12'
    ]
)

