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

class Fame:
    __min = -600000
    __max = 600000
    faction = {'kami': 0, 'karavan': 0}
    nation = {'fyros': 0, 'matis': 0, 'tryker': 0, 'zorai': 0}

    def __init__(self, it):
        for f in it:
            if f.tag in self.faction:
                self.faction[f.tag] = self.clamp(f.text)
            if f.tag in self.nation:
                self.nation[f.tag] = self.clamp(f.text)

    def clamp(self, value):
        return sorted((self.__min, int(value), self.__max))[1]

class Allegiance:
    faction = None
    nation = None

    def __init__(self, faction=None, nation=None):
        if faction in Fame.faction:
            self.faction = faction
        if nation in Fame.nation:
            self.nation = nation
