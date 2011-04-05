"""
Flask-BGCSRF
"""

from setuptools import setup


setup(
    name='flask-bgcsrf',
    version='0.1',
    url='http://qotd.github.com/flask-bgcsrf',
    license='MIT',
    author='Baishampayan Ghose',
    author_email='b.ghose@qotd.co',
    description='A bad-ass Flask extension for adding CSRF protection.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>0.1'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ]
)
