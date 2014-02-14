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

import re

available_tags = (
    # Armors
    ('armor', re.compile('^ic[mtzfoc]a')),
    ('boots', re.compile('^ic[mtzfoc]a[lmh]b')),
    ('gloves', re.compile('^ic[mtzfoc]a[lmh]g')),
    ('pants', re.compile('^ic[mtzfoc]a[lmh]p')),
    ('sleeves', re.compile('^ic[mtzfoc]a[lmh]s')),
    ('vest', re.compile('^ic[mtzfoc]a[lmh]v')),
    ('helmet', re.compile('^ic[mtzfoc]a[lmh]h')),
    ('light_armor', re.compile('^ic[mtzfoc]al')),
    ('medium_armor', re.compile('^ic[mtzfoc]am')),
    ('heavy_armor', re.compile('^ic[mtzfoc]ah')),

    # Weapons
    ('weapon', re.compile('^ic[mtzfoc]m')),
    ('one_handed', re.compile('^ic[mtzfoc]m1')),
    ('two_handed', re.compile('^ic[mtzfoc]m2')),
    ('sword', re.compile('^ic[mtzfoc]m[12]ss[elbw]?')),
    ('mace', re.compile('^ic[mtzfoc]m[12]bm[elbw]?')),
    ('axe', re.compile('^ic[mtzfoc]m[12]sa[elbw]?')),
    ('spear', re.compile('^ic[mtzfoc]m[12]ps[elbw]?')),
    ('dagger', re.compile('^ic[mtzfoc]m[12]pd[elbw]?')),
    ('magic_amplifier', re.compile('^ic[mtzfoc]m[12]ms[elbw]?')),
    ('pike', re.compile('^ic[mtzfoc]m[12]pp[elbw]?')),
    # ('', re.compile('^ic[mtzfoc]m[12][elbw]?')),
    # ('', re.compile('^ic[mtzfoc]m[12][elbw]?')),
    # ('', re.compile('^ic[mtzfoc]m[12][elbw]?')),
    # ('', re.compile('^ic[mtzfoc]m[12][elbw]?')),
    # ('', re.compile('^ic[mtzfoc]m[12][elbw]?')),

    #Jewels
    ('jewel', re.compile('^ic[mtzfoc]j[abdepr]')),
    ('anklet', re.compile('^ic[mtzfoc]ja')),
    ('bracelet', re.compile('^ic[mtzfoc]jb')),
    ('diadem', re.compile('^ic[mtzfoc]jd')),
    ('earring', re.compile('^ic[mtzfoc]je')),
    ('pendant', re.compile('^ic[mtzfoc]jp')),
    ('ring', re.compile('^ic[mtzfoc]jr')),

    # Tools
    ('tool', re.compile('^it')),
    ('tool', re.compile('^ic[mtzfoc](kar|kam)t')),
    ('armor_tool', re.compile('^itarmor')),
    ('armor_tool', re.compile('^ic[mtzfoc](kar|kam)tarmor')),
    ('ammo_tool', re.compile('^itammo')),
    ('ammo_tool', re.compile('^ic[mtzfoc](kar|kam)tammo')),
    ('melee_weapon_tool', re.compile('^itmwea')),
    ('melee_weapon_tool', re.compile('^ic[mtzfoc](kar|kam)tmwea')),
    ('range_weapon_tool', re.compile('^itrwea')),
    ('range_weapon_tool', re.compile('^ic[mtzfoc](kar|kam)trwea')),
    ('jewel_tool', re.compile('^itjewel')),
    ('jewel_tool', re.compile('^ic[mtzfoc](kar|kam)tjewel')),
    ('tool_tool', re.compile('^ittool')),
    ('tool_tool', re.compile('^ic[mtzfoc](kar|kam)ttool')),
    ('pick', re.compile('^itforage')),
    ('pick', re.compile('^ic[mtzfoc](kar|kam)tforage')),

    # Misc items
    ('skin1', re.compile('^ic[mtzfoc].*_1$')),
    ('skin2', re.compile('^ic[mtzfoc].*_2$')),
    ('skin3', re.compile('^ic[mtzfoc].*_3$')),
    ('matis', re.compile('^icm')),
    ('tryker', re.compile('^ict')),
    ('zorai', re.compile('^icz')),
    ('fyros', re.compile('^icf')),

    # Misc materials
    ('material', re.compile('^m')),
    ('forest', re.compile('^m.*f\w\d{2}$')),
    ('lac', re.compile('^m.*l\w\d{2}$')),
    ('jungle', re.compile('^m.*j\w\d{2}$')),
    ('desert', re.compile('^m.*d\w\d{2}$')),
    ('prime_root', re.compile('^m.*p\w\d{2}$')),

    # Misc
    ('catalyser', re.compile('^ixpca01$')),
)
