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

from . import RYZOM_API_BASE_URL
from ryzomapi.exceptions import InvalidAPIKeyException
from ryzomapi.utils import api_key_is_valid
from ryzomapi.sas import get
try:
    from urllib.parse import urlencode
    from html import escape
except ImportError:
    from urllib import urlencode
    from cgi import escape

class Guild:
    __allowed = ('gid', 'name', 'race', 'icon', 'description', 'creation_date')

    def __init__(self, **kwargs):
        for k in kwargs:
            if k in self.__class__.__allowed:
                setattr(self, k, kwargs[k])
        if self.gid:
            self.gid = int(self.gid)
            self.id = self.gid

    def __str__(self):
        return self.name

    def icon_link(self, size='b', escape_url=False):
        params = urlencode({'size': size, 'icon': self.icon})
        ret = '%s/guild_icon.php?%s' % (RYZOM_API_BASE_URL, params)
        if escape_url:
            ret = escape(ret)
        return ret

def list_all(from_file=None):
    lst = []
    data = get('guilds', from_file=from_file)
    for node in data.findall('guild'):
        lst.append(Guild(gid = node.find('gid').text,
                         name = node.find('name').text,
                         race = node.find('race').text,
                         icon = node.find('icon').text,
                         creation_date = node.find('creation_date').text,
                         description = node.find('description').text))
    return lst

def get_by_key(api_key, from_file=None):
    if not api_key_is_valid(api_key, 'g'):
        raise InvalidAPIKeyException
    data = get('guild', apikey=api_key, from_file=from_file)
    node = data.find('guild')
    return Guild(gid = node.find('gid').text,
                 name = node.find('name').text,
                 race = node.find('race').text,
                 icon = node.find('icon').text,
                 creation_date = node.find('creation_date').text,
                 description = node.find('description').text)
