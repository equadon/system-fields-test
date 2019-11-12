# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# System Fields Test is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_indexer.api import RecordIndexer
from invenio_records_files.api import Record
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all, check_elasticsearch
from invenio_search import RecordsSearch

from system_fields_test.records.api import CustomRecord


def _(x):
    """Identity function for string extraction."""
    return x

RECORDS_REST_ENDPOINTS = {
    'recid': dict(
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        default_endpoint_prefix=True,
        record_class=CustomRecord,
        search_class=RecordsSearch,
        indexer_class=RecordIndexer,
        search_index='records',
        search_type=None,
        record_serializers={
            'application/json': ('system_fields_test.records.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('system_fields_test.records.serializers'
                                 ':json_v1_search'),
        },
        record_loaders={
            'application/json': ('system_fields_test.records.loaders'
                                 ':json_v1'),
        },
        list_route='/records/',
        item_route='/records/<pid(recid,'
                   'record_class="system_fields_test.records.api.CustomFilesRecord")'
                   ':pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=check_elasticsearch,
        update_permission_factory_imp=allow_all,
        delete_permission_factory_imp=allow_all,
        list_permission_factory_imp=allow_all
    ),
}
"""REST API for system-fields-test."""

RECORDS_UI_ENDPOINTS = {
    'recid': {
        'pid_type': 'recid',
        'route': '/records/<pid_value>',
        'template': 'records/record.html',
    },
    'recid_previewer': {
        'pid_type': 'recid',
        'route': '/records/<pid_value>/preview/<path:filename>',
        'view_imp': 'invenio_previewer.views:preview',
        'record_class': 'invenio_records_files.api:Record',
    },
    'recid_files': {
        'pid_type': 'recid',
        'route': '/records/<pid_value>/files/<path:filename>',
        'view_imp': 'invenio_records_files.utils:file_download_ui',
        'record_class': 'invenio_records_files.api:Record',
    },
}
"""Records UI for system-fields-test."""

SEARCH_UI_JSTEMPLATE_RESULTS = 'templates/records/results.html'
"""Result list template."""

PIDSTORE_RECID_FIELD = 'id'

SYSTEM_FIELDS_TEST_ENDPOINTS_ENABLED = True
"""Enable/disable automatic endpoint registration."""


RECORDS_REST_FACETS = dict(
    records=dict(
        aggs=dict(
            type=dict(terms=dict(field='type')),
            keywords=dict(terms=dict(field='keywords'))
        ),
        post_filters=dict(
            type=terms_filter('type'),
            keywords=terms_filter('keywords'),
        )
    )
)
"""Introduce searching facets."""


RECORDS_REST_SORT_OPTIONS = dict(
    records=dict(
        bestmatch=dict(
            title=_('Best match'),
            fields=['_score'],
            default_order='desc',
            order=1,
        ),
        mostrecent=dict(
            title=_('Most recent'),
            fields=['-_created'],
            default_order='asc',
            order=2,
        ),
    )
)
"""Setup sorting options."""


RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(
        query='bestmatch',
        noquery='mostrecent',
    )
)
"""Set default sorting options."""

RECORDS_FILES_REST_ENDPOINTS = {
    'RECORDS_REST_ENDPOINTS': {
        'recid': '/files'
    },
}
"""Records files integration."""

FILES_REST_PERMISSION_FACTORY = \
    'system_fields_test.records.permissions:files_permission_factory'
"""Files-REST permissions factory."""
