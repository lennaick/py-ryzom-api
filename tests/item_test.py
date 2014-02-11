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
        i = Item()
        self.assertEquals(i.sheet, None)

        i = Item('iczahp_3.sitem')
        self.assertEquals(i.sheet, 'iczahp_3')
        self.assertEquals(i.icon_url(), '%s/item_icon.php?sheetid=iczahp_3' % RYZOM_API_BASE_URL)

    def test_sheetid_filter(self):
        self.assertEquals(Item('icokamm2ms_1.sitem').sheet, 'icokamm2ms_1')
        self.assertEquals(Item('icokamm2ms_1').sheet, 'icokamm2ms_1')
        self.assertEquals(Item('lolsitem').sheet, 'lolsitem')
        self.assertEquals(Item('.sitem').sheet, '.sitem')
        self.assertEquals(Item('').sheet, None)

    def test_equality(self):
        i1 = Item('iczahp_3')
        i2 = Item('iczahp_3.sitem')
        i3 = Item('icokamm2ms_1.sitem')

        self.assertEquals(i1, i2)
        self.assertNotEquals(i1, i3)
        self.assertNotEquals(i2, i3)
        self.assertEquals(i1 == i2, True)
        self.assertEquals(i1 != i2, False)
        self.assertEquals(i1 == i3, False)
        self.assertEquals(i1 != i3, True)

        i1.quality = 250
        self.assertNotEquals(i1, i2)
        i2.quality = 250
        self.assertEquals(i1, i2)

if __name__ == '__main__':
    unittest.main()
