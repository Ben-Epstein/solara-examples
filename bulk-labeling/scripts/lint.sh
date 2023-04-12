#!/bin/sh -ex

mypy bulk_labeling
flake8 bulk_labeling
black bulk_labeling --check
isort bulk_labeling --check-only
