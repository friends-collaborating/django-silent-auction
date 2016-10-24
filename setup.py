"""Setup script of django-silent-auction"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages
import silent_auction

setup(
    name='silent-auction',
    version=silent_auction.__version__,

    description='Django Silent Auction package',
    long_description='Django Silent Auction package',
    keywords='django, auction',

    author=silent_auction.__author__,
    author_email=silent_auction.__email__,
    url=silent_auction.__url__,

    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license=silent_auction.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django==1.10.1',
        'djangorestframework==3.4.7',
        'Markdown==2.6.7',
        'django-filter==0.15.3',
        'django_parler==1.6.5',
        'django-parler-rest==1.4.2',
        'django-versatileimagefield==1.6',
    ],
)
