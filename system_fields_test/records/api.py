# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# System Fields Test is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Flask extension for System Fields Test."""

import copy

from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import Record
from invenio_records_files.api import Record as FilesRecord


class CustomRecord(Record):

    _schema = "records/record-v1.0.0.json"
    _system_fields = None

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        data["id"] = int(data["id"])
        data["$schema"] = current_jsonschemas.path_to_url(cls._schema)
        return super(CustomRecord, cls).create(data, id_=id_, **kwargs)

    def clear(self):
        values = self.copy()
        super(CustomRecord, self).clear()
        abc = values


class CustomFilesRecord(FilesRecord):

    _schema = "records/record-v1.0.0.json"
    _system_fields = ["$schema"]

    @classmethod
    def create(cls, data, id_=None, **kwargs):
        data["id"] = int(data["id"])
        data["$schema"] = current_jsonschemas.path_to_url(cls._schema)
        return super(CustomRecord, cls).create(data, id_=id_, **kwargs)

    def clear(self):
        values = copy.deepcopy(self)
        super(CustomFilesRecord, self).clear()
        if self._system_fields:
            for field in self._system_fields:
                self[field] = values[field]

    def update(self, data):
        super(CustomFilesRecord, self).update(data)
        self["id"] = int(self["id"])
