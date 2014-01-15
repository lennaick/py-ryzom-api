# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

from distutils.core import setup

setup(
    name = 'ryzomapi',
    packages = ['ryzomapi'],
    version = '0.0.1',
    description = 'Unofficial python Ryzom API',
    author = 'Rodolphe Breard',
    author_email = 'rodolphe@what.tf',
    url = 'https://github.com/TychoBrahe/py-ryzom-api',
    keywords = ['ryzom', 'api'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Topic :: Software Development",
    ]
)
