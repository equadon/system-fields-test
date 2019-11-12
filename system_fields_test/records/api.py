# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# System Fields Test is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Flask extension for System Fields Test."""

from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import Record


class CustomRecord(Record):

    _schema = "records/record-v1.0.0.json"

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        # import wdb; wdb.set_trace()
        data["id"] = int(data["id"])
        data["$schema"] = current_jsonschemas.path_to_url(cls._schema)
        # data["$schema"] = "http://www.test.com/"
        # return super(CustomRecord, cls).create(data, id_=id_, **kwargs)
        return super(CustomRecord, cls).create(data, id_=id_, **kwargs)
