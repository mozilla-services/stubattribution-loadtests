[![Build Status](https://travis-ci.org/stephendonner/stubattribution-loadtests.svg?branch=master)](https://travis-ci.org/stephendonner/stubattribution-loadtests)
[![updates](https://pyup.io/repos/github/stephendonner/stubattribution-loadtests/shield.svg)](https://pyup.io/repos/github/stephendonner/stubattribution-loadtests/)
[![Python 3](https://pyup.io/repos/github/stephendonner/stubattribution-loadtests/python-3-shield.svg)](https://pyup.io/repos/github/stephendonner/stubattribution-loadtests/)


# stubattribution-loadtests

generic load test based on molotov: https://github.com/loads/molotov

## Requirements

- Python 3.5+


## How to run the loadtest?

### For STAGE 

    molotov -cx -d 1 loadtest.py

## How to build the docker image?

    make docker-build


## How to run the docker image?

    make docker-run


## How to clean the repository?

    make clean
