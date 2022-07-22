#!/usr/bin/env bash
python parse_field_documentation.py
#cp build/latex/opencoin.pdf docs
make clean
make html
rsync -r build/html/ baach:opencoin/0.4
#rsync build/latex/opencoin.pdf baach:opencoin/0.4