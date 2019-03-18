#!/bin/sh

set -e

echo "Linting code..."
flake8 src
mypy --ignore-missing-imports src
bandit -r src

echo "Running tests with nose..."
nosetests -s -x -v --with-coverage --cover-erase --cover-package=IndexRunner --cover-html --cover-html-dir=./test_coverage --nocapture  --nologcapture src/test
