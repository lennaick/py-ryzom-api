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
            # materials
            # - op
            Item('m0741dxacc01'),
            Item('m0743dxacc01'),
            Item('m0753dxacc01'),
            Item('m0755dxacc01'),
            # - blade, point
            Item('m0016dxape01'),
            Item('m0067ckdjd01.sitem'),
            Item('m0106ccepe01.sitem'),
            Item('m0680cbcld01'),
            # - hammer, counterweight
            Item('m0025chcld01.sitem'),
            Item('m0100dxaje01.sitem'),
            Item('m0515chrfe01'),
            Item('m0662dxape01'),
            # - shaft, ammo_bullet
            Item('m0136ccdjd01'),
            Item('m0384ccldd01'),
            Item('m0497dxapf01.sitem'),
            Item('m0600ckfjd01.sitem'),
            # - barrel, armor_shell
            Item('m0040dxapf01.sitem'),
            Item('m0376cckfc01.sitem'),
            Item('m0469chwdd01.sitem'),
            Item('m0485ckape01.sitem'),
            # - ammo_jacket, lining
            Item('m0046dxapf01'),
            Item('m0083chgdd01'),
            Item('m0511chbpd01.sitem'),
            Item('m0640cpcfe01.sitem'),
            # - explosive, stuffing
            Item('m0103dxape01'),
            Item('m0135ccdfd01.sitem'),
            Item('m0366cbcld01'),
            Item('m0557ccnpe01.sitem'),
            # - firing_pin, armor_clip
            Item('m0074ckede01'),
            Item('m0109dxale01'),
            Item('m0603ckffd01'),
            Item('m0641ccepe01'),
            # - trigger, jewel_setting
            Item('m0023dxapf01.sitem'),
            Item('m0149chlpd01.sitem'),
            Item('m0615chvcb01.sitem'),
            Item('m0677chuje01.sitem'),
            # - grip, clothes
            Item('m0006dxacb01'),
            Item('m0118dxapf01'),
            Item('m0367chnfd01'),
            Item('m0553chxpd01'),
            # - jewel, magic_focus
            Item('m0015dxaje01'),
            Item('m0148chlpe01'),
            Item('m0474cpcpe01'),
            Item('m0675chujd01'),
            # kitin larva
            Item('m0312dxacf01'),
            # shields
            Item('icmss_2'),
            Item('icmsbl'),
            # tools
            Item('icokartarmor_1'),
            Item('itammo'),
            Item('icokartmwea_2.sitem'),
            Item('icokartrwea_2.sitem'),
            Item('icokartjewel_1.sitem'),
            Item('ittool.sitem'),
            Item('icokartforage_1.sitem'),
            # jewels
            Item('icfjb'),
            Item('icfjp.sitem'),
            Item('icfjr'),
            Item('ictjb.sitem'),
            Item('ictjb_3.sitem'),
            # piece of kitin
            Item('slaughter_week_token.sitem'),
            # enchantments
            Item('crystalized_spell.sitem'),
            Item('item_sap_recharge'),
            Item('light_sap_recharge.sitem'),
            # pets
            Item('iapf'),
            Item('iapsff.sitem'),
            Item('iasf.sitem'),
            # marauder crystal
            Item('marauder_teleport_crystal.sitem'),
            # job items
            Item('rpjobitem_201_a0'),
            Item('rpjobitem_201_b0'),
            Item('rpjobitem_201_c5'),
            Item('rpjobitem_206_c1.sitem'),
            # consumables items
            Item('conso_fireworks_c'),
            Item('conso_fireworks_g.sitem'),
            Item('conso_fireworks_j.sitem'),
            Item('ipk_minor_life'),
            Item('ipoc_dex'),
            Item('ipoc_met'),
            Item('ipop_elc'),
            # catalysers
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
