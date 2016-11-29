# BetterBib

[![Build Status](https://travis-ci.org/nschloe/betterbib.svg?branch=master)](https://travis-ci.org/nschloe/betterbib)
[![Code Health](https://landscape.io/github/nschloe/betterbib/master/landscape.png)](https://landscape.io/github/nschloe/betterbib/master)
[![codecov](https://codecov.io/gh/nschloe/betterbib/branch/master/graph/badge.svg)](https://codecov.io/gh/nschloe/betterbib)
[![PyPi Version](https://img.shields.io/pypi/v/betterbib.svg)](https://pypi.python.org/pypi/betterbib)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/betterbib.svg?style=social&label=Star&maxAge=2592000)](https://github.com/nschloe/betterbib)

BibTeX files are typically manually maintained and thus often contain
inconsistencies, mistakes, or are missing information. BetterBib helps
maintaining your BibTeX files by comparing them with online sources and
correcting whatever entries are found faulty. For example, with
```
$ betterbib in.bib out.bib
```
the input BibTex
```
@article {krylov,
  author = {Liesen and Gaul and Nabben},
  title = {Deflation Krylov Augmented}
}
```
is converted into
```
@article{krylov,
  author = {Gaul, André and Gutknecht, Martin H. and Liesen, Jörg and Nabben, Reinhard},
  publisher = {Society for Industrial & Applied Mathematics (SIAM)},
  doi = {10.1137/110820713},
  title = {A Framework for Deflated and Augmented Krylov Subspace Methods},
  url = {http://dx.doi.org/10.1137/110820713},
  journal = {SIAM. J. Matrix Anal. & Appl.},
  number = {2},
  month = apr,
  volume = {34},
  source = {CrossRef},
  year = {2013},
  pages = {495-518}
}
```

BetterBib fetches data from [CrossRef](http://www.crossref.org/).

All BetterBib command-line options are explained in `betterbib -h`.


### Installation

#### Python Package Index

BetterBib is [available from the Python Package
Index](https://pypi.python.org/pypi/betterbib/), so simply type
```
pip install betterbib
```
to install or
```
pip install betterbib -U
```
to upgrade.

#### Manual installation

Download BetterBib from [GitHub](https://github.com/nschloe/betterbib) and
install it with
```
python setup.py install
```

### Requirements

BetterBib has a few Python dependencies, all listed in `requirement.txt`,
notably:

* [Pybtex](http://pybtex.sourceforge.net/),
* [requests](http://docs.python-requests.org/en/latest/),

Additionally, BetterBib requires

* [pandoc](https://pandoc.org/)

to be installed.


### Usage
```
$ ./betterbib mybibliography.bib out.bib
```

### Testing

To run the BetterBib unit tests, check out this repository and type
```
pytest
```


### Distribution
To create a new release

1. bump the `__version__` number,

2. publish to PyPi and tag on GitHub:
    ```
    $ make publish
    ```

### License

BetterBib is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
