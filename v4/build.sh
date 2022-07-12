#!/usr/bin/env bash
python parse_field_documentation.py
make clean
make html
rsync -r build/html/ baach:opencoin/0.4