#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports bulk_labeling

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place bulk_labeling --exclude=__init__.py
# For some reason we need to run this again so that black can get it into the format we want
isort bulk_labeling
black bulk_labeling
