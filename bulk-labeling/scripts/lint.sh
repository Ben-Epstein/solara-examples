#!/bin/sh -ex

mypy bulk_labeling
flake8 bulk_labeling --max-line-length=88
black bulk_labeling --check
isort bulk_labeling --check-only
