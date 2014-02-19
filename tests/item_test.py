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

        ordered_items = [
            # armors
            Item('iccalb.sitem'),
            Item('icmalb_3.sitem'),
            Item('iccalg.sitem'),
            Item('icmacp_3.sitem'),
            Item('ictalv_3.sitem'),
            Item('icmamg_3.sitem'),
            Item('icmams_3.sitem'),
            Item('icmahv_2.sitem'),
            Item('ictahh_3.sitem'),
            # melee weapons
            Item('icmm1ss_3.sitem'),
            Item('icmm1sa_3.sitem'),
            Item('icfm1ps'),
            Item('icbm1bs.sitem'),
            Item('iccm2ss.sitem'),
            Item('icmm2pp'),
            Item('icokarm2pp_1.sitem'),
            Item('ictm2ms_3.sitem'),
            Item('iczm2ms.sitem'),
            # range weapons
            Item('icmr2a.sitem'),
            Item('icfr2l.sitem'),
            Item('iczr2l.sitem'),
            Item('icmr1p'),
            Item('ictr2r.sitem'),
            # ammo
            Item('iczp2lb.sitem'),
            Item('iczp2lp.sitem'),
            Item('icmp1pb.sitem'),
            Item('iczp1pp'),
            Item('iczp2rp'),
            # jewels
            Item('icfjb'),
            Item('icfjp.sitem'),
            Item('icfjr'),
            Item('ictjb.sitem'),
            Item('ictjb_3.sitem'),
            # tools
            Item('icokartarmor_1'),
            Item('itammo'),
            Item('icokartmwea_2.sitem'),
            Item('icokartrwea_2.sitem'),
            Item('icokartjewel_1.sitem'),
            Item('ittool.sitem'),
            Item('icokartforage_1.sitem'),
            # misc
            Item('ixpca01.sitem'),
        ]
        self.assertTrue(all(ordered_items[i] < ordered_items[i + 1] for i in range(len(ordered_items) - 1)))

    def test_armor(self):
        self.assertIn('armor', Item('iccalg.sitem').tags)
        self.assertIn('light_armor', Item('iccalg.sitem').tags)
        self.assertIn('gloves', Item('iccalg.sitem').tags)

        self.assertIn('armor', Item('icmamv_3.sitem').tags)
        self.assertIn('medium_armor', Item('icmamv_3.sitem').tags)
        self.assertIn('vest', Item('icmamv_3.sitem').tags)
        self.assertIn('matis', Item('icmamv_3.sitem').tags)
        self.assertIn('skin3', Item('icmamv_3.sitem').tags)

        self.assertIn('armor', Item('ictahh_3').tags)
        self.assertIn('heavy_armor', Item('ictahh_3').tags)
        self.assertIn('helmet', Item('ictahh_3').tags)
        self.assertIn('tryker', Item('ictahh_3').tags)

    def test_jewels(self):
        self.assertIn('jewel', Item('icfjr').tags)
        self.assertIn('fyros', Item('icfjr').tags)
        self.assertIn('ring', Item('icfjr').tags)

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
