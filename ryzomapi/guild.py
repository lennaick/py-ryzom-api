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
from ryzomapi.apikey import api_key_is_valid
from ryzomapi.datetime import RyzomDate
from ryzomapi.fame import Fame
from ryzomapi.sas import get
try:
    from urllib.parse import urlencode
    from html import escape
except ImportError:
    from urllib import urlencode
    from cgi import escape
import datetime

class Guild:
    __allowed = ('gid', 'name', 'race', 'icon', 'description', 'creation_date',
                 'shard', 'motd', 'money')

    def __init__(self, api_key=None, from_file=None):
        if api_key is not None or from_file is not None:
            self.load(api_key, from_file)

        if hasattr(self, 'creation_date'):
            self.creation_date = RyzomDate(self.creation_date)
        if hasattr(self, 'gid'):
            self.gid = int(self.gid)
            self.id = self.gid

    def __str__(self):
        return self.name

    def load(self, api_key, from_file):
        if from_file is None and not api_key_is_valid(api_key, 'g'):
            raise InvalidAPIKeyException
        data = get('guild', apikey=api_key, from_file=from_file)
        node = data.find('guild')
        for attr_name in self.__allowed:
            dt = node.find(attr_name)
            if dt is not None:
                setattr(self, attr_name, dt.text)
        fame = node.find('fame')
        if fame is not None:
            setattr(self, 'fame', Fame(fame))

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
        guild = Guild()
        for attr_name in ('gid', 'name', 'race', 'icon', 'creation_date', 'description'):
            setattr(guild, attr_name, node.find(attr_name).text)
        lst.append(guild)
    return lst
