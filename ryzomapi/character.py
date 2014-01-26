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

from ryzomapi.exceptions import InvalidAPIKeyException
from ryzomapi.apikey import api_key_is_valid
from ryzomapi.fame import Fame, Allegiance
from ryzomapi.sas import get

class Character:
    __allowed = ('id', 'name', 'shard', 'race', 'gender')

    def __init__(self, api_key=None, from_file=None):
        if api_key is not None or from_file is not None:
            self.load(api_key, from_file)

        if hasattr(self, 'creation_date'):
            self.creation_date = RyzomDate(self.creation_date)
        if hasattr(self, 'id'):
            self.id = int(self.id)

    def __str__(self):
        return self.name

    def load(self, api_key, from_file):
        if from_file is None and not api_key_is_valid(api_key, 'c'):
            raise InvalidAPIKeyException
        data = get('character', apikey=api_key, from_file=from_file)
        node = data.find('character')

        for attr_name in self.__allowed:
            dt = node.find(attr_name)
            if dt is not None:
                setattr(self, attr_name, dt.text)

        fame = node.find('fame')
        if fame is not None:
            setattr(self, 'fame', Fame(fame))

        faction = node.find('cult').text if node.find('cult') is not None else None
        nation = node.find('civilization').text if node.find('civilization') is not None else None
        self.allegiance = Allegiance(faction, nation)
