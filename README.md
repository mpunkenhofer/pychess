# pychess
[![Build Status](https://travis-ci.org/mpunkenhofer/pychess.svg?branch=master)](https://travis-ci.org/mpunkenhofer/pychess)
[![codecov](https://codecov.io/gh/mpunkenhofer/pychess/branch/master/graph/badge.svg)](https://codecov.io/gh/mpunkenhofer/pychess)

A simple python chess library.

I started this project just for fun - being a chess fan i always wanted to code a chess game client but the last time i
started (in c++) i eventually got stuck at dealing with absolute pins and never finished. This time tough i went all the
way and even added over 200 tests (went for close to 100% coverage) to make sure i get everything right and learn a
thing or two along the way.

## Installation
Installation requirements: [https://packaging.python.org/tutorials/installing-packages/#id10](https://packaging.python.org/tutorials/installing-packages/#id10)
```
python setup.py install
```

## Examples
Currently i have only a primitive client with a console interface which helped me during implementation to show for.
I plan to add more examples in the future - at least one with a graphical user interface.

## Tests
For testing i used python [unittest](https://docs.python.org/3/library/unittest.html) and tested the implementation
with Python 3.5 and 3.6.

If you have pychess installed you should be able to run:
```
python -m unittest discover
```

## Documentation
Sadly since this was just a quick little project during holidays there is no documentation really. But you can take
a look at the examples and tests to figure things out.


## Attributions
Chess piece graphics have been taken from 
[here](https://commons.wikimedia.org/wiki/File:Chess_Pieces_Sprite.svg). Author/User: jurgenwesterhof (adapted from work of Cburnett)
