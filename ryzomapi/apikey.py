##
## Copyright (c) 2014 Rodolphe Breard
## 
## Permission to use, copy, modify, and/or distribute this software for any
## purpose with or without fee is hereby granted, provided that the above
## copyright notice and this permission notice appear in all copies.
## 
## THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
## WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
## MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
## ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
## WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
## ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
## OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
##

from . import api_key_pattern
import re

def api_key_is_valid(api_key, key_type):
    """Check whether an API Key is valid or not.

    :param api_key: the api key to check
    :type api_key: str
    :param key_type: the api key type ('g' for guild, 'c' for character)
    :type key_type: str
    :returns: bool
    """
    if not re.match(api_key_pattern, api_key):
        return False
    if api_key[0] != key_type:
        return False
    return True

def character_api_key_is_valid(api_key):
    """Check whether a character API Key is valid or not."""
    return api_key_is_valid(api_key, 'c')

def guild_api_key_is_valid(api_key):
    """Check whether a guild API Key is valid or not."""
    return api_key_is_valid(api_key, 'g')
