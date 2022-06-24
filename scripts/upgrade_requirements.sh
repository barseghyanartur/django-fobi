#!/usr/bin/env bash
cd examples/requirements/
pip-compile benchmarks.in --upgrade
pip-compile common.in --upgrade
pip-compile debug.in --upgrade
pip-compile deployment.in --upgrade
pip-compile dev.in --upgrade
pip-compile django_2_2.in --upgrade
pip-compile django_3_0.in --upgrade
pip-compile django_3_1.in --upgrade
pip-compile django_3_2.in --upgrade
pip-compile docs.in --upgrade
pip-compile style_checkers.in --upgrade
pip-compile test.in --upgrade
pip-compile testing.in --upgrade
