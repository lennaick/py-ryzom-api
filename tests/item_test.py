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
        self.assertIsNone(i.sheet)

        i = Item('iczahp_3.sitem')
        self.assertEquals(i.sheet, 'iczahp_3')
        self.assertEquals(i.icon_url(), '%s/item_icon.php?sheetid=iczahp_3.sitem' % RYZOM_API_BASE_URL)

    def test_sheetid_filter(self):
        self.assertEquals(Item('icokamm2ms_1.sitem').sheet, 'icokamm2ms_1')
        self.assertEquals(Item('icokamm2ms_1').sheet, 'icokamm2ms_1')
        self.assertEquals(Item('lolsitem').sheet, 'lolsitem')
        self.assertEquals(Item('.sitem').sheet, '.sitem')
        self.assertIsNone(Item('').sheet)

    def test_comparison(self):
        i1 = Item('iczahp_3')
        i2 = Item('iczahp_3.sitem')
        i3 = Item('icokamm2ms_1.sitem')

        self.assertEquals(i1, i2)
        self.assertNotEquals(i1, i3)
        self.assertNotEquals(i2, i3)
        self.assertTrue(i1 == i2)
        self.assertFalse(i1 != i2)
        self.assertFalse(i1 == i3)
        self.assertTrue(i1 != i3)

        i1.quality = 250
        self.assertNotEquals(i1, i2)
        self.assertTrue(i1 > i2)
        self.assertTrue(i1 >= i2)
        self.assertFalse(i1 < i2)
        self.assertFalse(i1 <= i2)

        i2.quality = 250
        self.assertEquals(i1, i2)
        self.assertFalse(i1 > i2)
        self.assertTrue(i1 >= i2)
        self.assertFalse(i1 < i2)
        self.assertTrue(i1 <= i2)

    def test_jewels(self):
        self.assertIn('jewel', Item('icfjr.').tags)
        self.assertIn('fyros', Item('icfjr.').tags)
        self.assertIn('ring', Item('icfjr.').tags)

        self.assertIn('jewel', Item('ictjp_3.sitem').tags)
        self.assertIn('tryker', Item('ictjp_3.sitem').tags)
        self.assertIn('skin3', Item('ictjp_3.sitem').tags)
        self.assertIn('pendant', Item('ictjp_3.sitem').tags)

        self.assertIn('jewel', Item('icmja').tags)
        self.assertIn('matis', Item('icmja').tags)
        self.assertIn('anklet', Item('icmja').tags)

    def test_tools(self):
        self.assertIn('tool', Item('itforage').tags)
        self.assertIn('pick', Item('itforage').tags)

        self.assertIn('tool', Item('ittool.sitem').tags)
        self.assertIn('tool_tool', Item('ittool.sitem').tags)

        self.assertIn('tool', Item('icokartforage_1').tags)
        self.assertIn('pick', Item('icokartforage_1').tags)
        self.assertIn('skin1', Item('icokartforage_1').tags)

if __name__ == '__main__':
    unittest.main()
