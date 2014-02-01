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

import sys
sys.path.insert(0, '.')

from ryzomapi.exceptions import InvalidAPIKeyException
from ryzomapi import RYZOM_API_BASE_URL, Guild
import xml.etree
import unittest

class GuildsTest(unittest.TestCase):
    def test_all_loading(self):
        lst = Guild.list_all(from_file='tests/data/guild_1.xml')
        self.assertEqual(len(lst), 3)

        self.assertIn(lst[0].icon_url(), ('%s/guild_icon.php?icon=544929668269603272&size=b' % RYZOM_API_BASE_URL,
                                          '%s/guild_icon.php?size=b&icon=544929668269603272' % RYZOM_API_BASE_URL))
        self.assertIn(lst[0].icon_url(escape_url=True), ('%s/guild_icon.php?icon=544929668269603272&amp;size=b' % RYZOM_API_BASE_URL,
                                                         '%s/guild_icon.php?size=b&amp;icon=544929668269603272' % RYZOM_API_BASE_URL))

        lst = Guild.list_all(from_file='tests/data/guild_2.xml')
        self.assertEqual(len(lst), 0)

    def test_all_invalid_data(self):
        with self.assertRaises(xml.etree.ElementTree.ParseError):
            lst = Guild.list_all(from_file='tests/data/invalid.xml')

        with self.assertRaises(xml.etree.ElementTree.ParseError):
            lst = Guild.list_all(from_file='tests/data/empty.xml')

    def test_guild_loading(self):
        guild = Guild(from_file='tests/data/guild_3.xml')
        self.assertEqual(guild.gid, 4242)
        self.assertEqual(guild.id, 4242)
        self.assertEqual(guild.name, 'The Test Guild')
        self.assertEqual(guild.icon, '110142619738866353')

    def test_guild_invalid_data(self):
        with self.assertRaises(InvalidAPIKeyException):
            Guild('')

        with self.assertRaises(InvalidAPIKeyException):
            Guild('invalid key')

if __name__ == '__main__':
    unittest.main()
