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
from ryzomapi.sas import get

class Guild:
    def __init__(self, gid, name, race, icon, creation_date, description):
        self.gid = int(gid)
        self.name = str(name)
        self.race = str(race)
        self.icon = str(icon)
        self.creation_date = str(creation_date)
        self.description = str(description)

    def __str__(self):
        return self.name

def list_all():
    lst = []
    data = get('guilds')
    for node in data.findall('guild'):
        lst.append(Guild(node.find('gid').text,
                         node.find('name').text,
                         node.find('race').text,
                         node.find('icon').text,
                         node.find('creation_date').text,
                         node.find('description').text))
    return lst
