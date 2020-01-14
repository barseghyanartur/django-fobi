#!/usr/bin/env bash
cd examples/simple/
./manage.py collectstatic --no-input  "$@"
