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

RYZOM_API_DOMAIN = 'api.ryzom.com'
RYZOM_API_BASE_URL = 'http://%s' % RYZOM_API_DOMAIN

__all__ = [
    'apikey',
    'character',
    'exceptions',
    'datetime',
    'fame',
    'guild',
    'sas'
]

import re
api_key_pattern = re.compile('^(g|c)[a-f0-9]{40}$')


from . import exceptions
from . import datetime
from . import apikey
from . import fame
from . import sas

try:
    from urllib.parse import urlencode
    from html import escape
except ImportError:
    from urllib import urlencode
    from cgi import escape


class Character:
    __allowed = ('id', 'name', 'shard', 'race', 'gender')

    def __init__(self, api_key=None, from_file=None):
        if api_key is not None or from_file is not None:
            self.load(api_key, from_file)

        if hasattr(self, 'id'):
            self.id = int(self.id)

    def __str__(self):
        return self.name

    def load(self, api_key, from_file):
        if from_file is None and not apikey.api_key_is_valid(api_key, 'c'):
            raise exceptions.InvalidAPIKeyException
        data = sas.get('character', apikey=api_key, from_file=from_file)
        node = data.find('character')

        for attr_name in self.__allowed:
            dt = node.find(attr_name)
            if dt is not None:
                setattr(self, attr_name, dt.text)

        f = node.find('fame')
        if f is not None:
            setattr(self, 'fame', fame.Fame(f))

        faction = node.find('cult').text if node.find('cult') is not None else None
        nation = node.find('civilization').text if node.find('civilization') is not None else None
        setattr(self, 'allegiance', fame.Allegiance(faction, nation))


class Member:
    def __init__(self, name, grade=None, joined=None):
        self.name = name
        if grade is not None:
            self.grade = grade
        if joined is not None:
            self.joined = joined


class Guild:
    __allowed = ('gid', 'name', 'race', 'icon', 'description', 'creation_date',
                 'shard', 'motd', 'money')

    def __init__(self, api_key=None, from_file=None):
        if api_key is not None or from_file is not None:
            self.load(api_key, from_file)

        if hasattr(self, 'creation_date'):
            self.creation_date = datetime.RyzomDate(self.creation_date)
        if hasattr(self, 'gid'):
            self.gid = int(self.gid)
            self.id = self.gid

    def __str__(self):
        return self.name

    def load(self, api_key, from_file):
        if from_file is None and not apikey.api_key_is_valid(api_key, 'g'):
            raise exceptions.InvalidAPIKeyException
        data = sas.get('guild', apikey=api_key, from_file=from_file)
        node = data.find('guild')

        for attr_name in self.__allowed:
            dt = node.find(attr_name)
            if dt is not None:
                setattr(self, attr_name, dt.text)

        f = node.find('fame')
        if f is not None:
            setattr(self, 'fame', fame.Fame(f))

        faction = node.find('cult').text if node.find('cult') is not None else None
        nation = node.find('civilization').text if node.find('civilization') is not None else None
        self.allegiance = fame.Allegiance(faction, nation)

        members = node.find('members')
        if members is not None:
            setattr(self, 'members', [])
            for m in members.findall('member'):
                self.members.append(Member(m.find('name').text,
                                           m.find('grade').text,
                                           m.find('joined').text))

    def icon_link(self, size='b', escape_url=False):
        params = urlencode({'size': size, 'icon': self.icon})
        ret = '%s/guild_icon.php?%s' % (RYZOM_API_BASE_URL, params)
        if escape_url:
            ret = escape(ret)
        return ret

    @staticmethod
    def list_all(from_file=None):
        lst = []
        data = sas.get('guilds', from_file=from_file)
        for node in data.findall('guild'):
            guild = Guild()
            for attr_name in ('gid', 'name', 'race', 'icon', 'creation_date', 'description'):
                setattr(guild, attr_name, node.find(attr_name).text)
            lst.append(guild)
        return lst
