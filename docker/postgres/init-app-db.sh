#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# System Fields Test is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE system-fields-test WITH LOGIN PASSWORD 'system-fields-test';
    ALTER ROLE system-fields-test CREATEDB;
    \du;
EOSQL
