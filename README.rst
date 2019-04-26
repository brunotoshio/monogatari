========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/onigiri/badge/?style=flat
    :target: https://readthedocs.org/projects/onigiri
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/brunotoshio/onigiri.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/brunotoshio/onigiri

.. |coveralls| image:: https://coveralls.io/repos/brunotoshio/onigiri/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/brunotoshio/onigiri

.. |codecov| image:: https://codecov.io/github/brunotoshio/onigiri/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/brunotoshio/onigiri

.. |version| image:: https://img.shields.io/pypi/v/onigiri.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/onigiri

.. |commits-since| image:: https://img.shields.io/github/commits-since/brunotoshio/onigiri/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/brunotoshio/onigiri/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/onigiri.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/onigiri

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/onigiri.svg
    :alt: Supported versions
    :target: https://pypi.org/project/onigiri

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/onigiri.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/onigiri


.. end-badges

Tool for handling dictionaries

* Free software: MIT license

Installation
============

::

    pip install onigiri

Documentation
=============


https://onigiri.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
