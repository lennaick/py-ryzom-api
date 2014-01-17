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

from ryzomapi.guild import list_all
import xml.etree
import unittest

class GuildsTest(unittest.TestCase):
    def test_loading(self):
        lst = list_all(from_file='data/guild_1.xml')
        self.assertEqual(len(lst), 3)

        lst = list_all(from_file='data/guild_2.xml')
        self.assertEqual(len(lst), 0)

    def test_invalid_data(self):
        with self.assertRaises(xml.etree.ElementTree.ParseError):
            lst = list_all(from_file='data/invalid.xml')

        with self.assertRaises(xml.etree.ElementTree.ParseError):
            lst = list_all(from_file='data/empty.xml')

if __name__ == '__main__':
    unittest.main()
