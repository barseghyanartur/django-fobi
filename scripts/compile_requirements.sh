#!/usr/bin/env bash
cd examples/requirements/
pip-compile captcha.in "$@"
pip-compile common.in "$@"
pip-compile debug.in "$@"
pip-compile demo.in "$@"
pip-compile deployment.in "$@"
pip-compile dev.in "$@"
pip-compile django_2_2.in "$@"
pip-compile django_3_0.in "$@"
pip-compile django_3_1.in "$@"
pip-compile django_3_2.in "$@"
pip-compile django_4_0.in "$@"
pip-compile django_4_1.in "$@"
pip-compile djangocms_3_4_3.in "$@"
pip-compile djangorestframework.in "$@"
pip-compile docs.in "$@"
pip-compile feincms_1_17.in "$@"
pip-compile feincms_1_20.in "$@"
pip-compile latest.in "$@"
pip-compile mptt.in "$@"
pip-compile recaptcha.in "$@"
pip-compile style_checkers.in "$@"
pip-compile test.in "$@"
pip-compile testing.in "$@"
pip-compile wagtail.in "$@"
