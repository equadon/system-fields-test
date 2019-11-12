# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# System Fields Test is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('system_fields_test', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='system-fields-test',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='system-fields-test Invenio',
    license='MIT',
    author='CERN',
    author_email='info@system-fields-test.com',
    url='https://github.com/system-fields-test/system-fields-test',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'system-fields-test = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'system_fields_test_records = system_fields_test.records:SystemFieldsTest',
        ],
        'invenio_base.blueprints': [
            'system_fields_test = system_fields_test.theme.views:blueprint',
            'system_fields_test_records = system_fields_test.records.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'system_fields_test_theme = system_fields_test.theme.webpack:theme',
        ],
        'invenio_config.module': [
            'system_fields_test = system_fields_test.config',
        ],
        'invenio_i18n.translations': [
            'messages = system_fields_test',
        ],
        'invenio_base.api_apps': [
            'system_fields_test = system_fields_test.records:SystemFieldsTest',
         ],
        'invenio_jsonschemas.schemas': [
            'system_fields_test = system_fields_test.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = system_fields_test.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
