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

from ryzomapi import RYZOM_API_BASE_URL, Item
import unittest

class ItemsTest(unittest.TestCase):
    def test_item_loading(self):
        i = Item('iczahp_3.sitem')
        self.assertEquals(i.sheetid, 'iczahp_3')

    def test_sheetid_filter(self):
        self.assertEquals(Item.filter_sheetid('icokamm2ms_1.sitem'), 'icokamm2ms_1')
        self.assertEquals(Item.filter_sheetid('icokamm2ms_1'), 'icokamm2ms_1')
        self.assertEquals(Item.filter_sheetid('lolsitem'), 'lolsitem')
        self.assertEquals(Item.filter_sheetid('.sitem'), '')
        self.assertEquals(Item.filter_sheetid(''), '')

if __name__ == '__main__':
    unittest.main()
