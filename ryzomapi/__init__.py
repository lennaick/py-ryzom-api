# -*- coding: utf-8 -*-
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
    'exceptions',
    'fame',
    'sas'
]

import re
api_key_pattern = re.compile('^(g|c)[a-f0-9]{40}$')


from . import exceptions
from . import fame
from . import sas

try:
    from urllib.parse import urlencode
    from html import escape
except ImportError:
    from urllib import urlencode
    from cgi import escape


class RyzomDate:
    __ticks_per_hour = 1800
    __hours_per_day = 24
    __days_per_week = 6
    __days_per_month = 30
    __month_per_cycle = 12
    __cycles_per_year = 4
    __start_year = 2567

    __offset = 61 * __hours_per_day * __ticks_per_hour
    __months = ('Winderly', 'Germinally', 'Folially', 'Floris', 'Medis', 'Thermis', 'Harvestor', 'Frutor', 'Fallenor', 'Pluvia', 'Mystia', 'Nivia')
    __days = ('Prima', 'Dua', 'Tria', 'Quarta', 'Quinteth', 'Holeth')
    __locales = {'en': {'ac': 'AC', 'num': ('st', 'nd', 'rd', 'th')},
                 'fr': {'ac': 'CA', 'num': ('er', 'nd', 'ème', 'ème')},
                 'de': {'ac': 'AZ', 'num': ('.', '.', '.', '.')}}

    def __init__(self, tick=None):
        if tick is None:
            tick = int(sas.get('time', format='xml').find('server_tick').text)
        self.locale_name = 'en'
        self.tick = int(tick)

        tick = self.tick - self.__offset
        hours = round(tick / self.__ticks_per_hour)
        days = round(hours / self.__hours_per_day)
        months = round(days / self.__days_per_month)
        cycles = round(months / self.__month_per_cycle)
        years = round(cycles / self.__cycles_per_year)

        self.year = self.__start_year + years
        self.cycle = cycles % self.__cycles_per_year
        self.month = self.__months[int(months % self.__month_per_cycle) - 1]
        self.day = days % self.__days_per_month
        self.hour = hours % self.__hours_per_day
        self.day_of_week = self.__days[int(self.day % self.__days_per_week) - 1]

    def __str__(self):
        self.cycle_numeral = self.__locales[self.locale_name]['num'][int(self.cycle) - 1]
        self.ac = self.__locales[self.locale_name]['ac']
        return '%(hour)dh - %(day_of_week)s, %(month)s %(day)d, %(cycle)d%(cycle_numeral)s %(ac)s %(year)d' % self.__dict__

    def locale(self, locale):
        if locale not in self.__locales:
            raise ValueError('%s: unknown locale' % locale)
        self.locale_name = locale
        return self


class APIKey:
    def __init__(self, api_key, key_type=None):
        self.key = str(api_key)

        if not re.match(api_key_pattern, self.key):
            raise exceptions.InvalidAPIKeyException

        if key_type is not None and not self.checkType(key_type):
            raise exceptions.InvalidAPIKeyException

    def __str__(self):
        return self.key

    def checkType(self, key_type):
        return self.key[0] == key_type.lower()[0]


class Item:
    __url_attrs = {'sheet': 'sheetid', 'quality': 'q', 'color': 'c', 'stack': 's', 'sap': 'sap', 'destroyed': 'destroyed'}

    def __init__(self, sheetid=None, xml=None):
        self.sheetid = self.filter_sheetid(sheetid)

    @staticmethod
    def filter_sheetid(sheetid):
        if sheetid is not None and sheetid[-6:] == '.sitem':
            sheetid = sheetid[:-6]
        return sheetid

    def icon_url(self, escape_url=False):
        params = {}
        for attr_name, url_name in self.__url_attrs.items():
            if hasattr(self, attr_name):
                params[url_name] = getattr(self, attr_name)
        ret = '%s/item_icon.php?%s' % (RYZOM_API_BASE_URL, urlencode(params))
        if escape_url:
            ret = escape(ret)
        return ret


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
        if from_file is None:
            api_key = APIKey(api_key, 'character')
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


class GuildMember:
    pass


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
        if hasattr(self, 'money'):
            self.money = int(self.money)

    def __str__(self):
        return self.name

    def load(self, api_key, from_file):
        if from_file is None:
            api_key = APIKey(api_key, 'guild')
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
                member = GuildMember()
                member.name = m.find('name').text
                member.grade = m.find('grade').text
                member.joined = RyzomDate(m.find('joined').text)
                self.members.append(member)

    def icon_url(self, size='b', escape_url=False):
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
