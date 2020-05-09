# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Gonzalo Peña-Castellanos (@goanpeca)
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""ZenHub API."""

from .core import ZenHubError, APILimitError, NotFoundError, InvalidTokenError, ZenHub


__version__ = "0.1.0.dev0"


def _to_version_info(version):
    """Convert a version string to a number and string tuple."""
    parts = []
    for part in version.split("."):
        try:
            part = int(part)
        except ValueError:
            pass

        parts.append(part)

    return tuple(parts)


VERSION_INFO = _to_version_info(__version__)
