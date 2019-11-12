# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# System Fields Test is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Flask extension for System Fields Test."""

from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import Record


class BaseRecord(Record):

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        data["$schema"] = current_jsonschemas.path_to_url(cls._schema)
        return super(BaseRecord, cls).create(data, id_=id_, **kwargs)
