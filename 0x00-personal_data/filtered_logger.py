#!/usr/bin/env python3
"""
function that return lod
g mess
"""


import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    return the log message obfuscated
    """
    for field in fields:
        msg_obfuscated = re.sub(field + "=.*?" + separator,
                                field + "=" + redaction + separator,
                                message)
    return msg_obfuscated
